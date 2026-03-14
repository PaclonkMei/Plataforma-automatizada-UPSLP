
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UsuarioForm

Usuario = get_user_model()

# ============================
# Vistas generales
# ============================

@login_required
def redireccion_por_rol(request):
    return redirect('bienvenida')  # Redirige a la página de bienvenida

@login_required
def bienvenida(request):
    return render(request, 'usuarios/bienvenida.html', {'usuario': request.user})

def no_autorizado(request):
    return render(request, 'usuarios/no_autorizado.html')

def inicio_publico(request):
    return render(request, 'usuarios/inicio_publico.html')


# ============================
# Helper para validar rol
# ============================
def es_admin(user):
    return user.is_authenticated and getattr(user, 'rol', '') == 'administrador'


# ============================
# CRUD para Administrador
# ============================

@login_required
def listar_usuarios(request):
    if not es_admin(request.user):
        messages.error(request, "No tienes permisos para acceder a esta sección.")
        return redirect('no_autorizado')

    q = request.GET.get('q', '').strip()
    usuarios = Usuario.objects.all().order_by('username')
    if q:
        usuarios = usuarios.filter(username__icontains=q)

    return render(request, 'usuarios/listar.html', {'usuarios': usuarios, 'q': q})


@login_required
def crear_usuario(request):
    if not es_admin(request.user):
        messages.error(request, "No tienes permisos para crear usuarios.")
        return redirect('no_autorizado')

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('usuarios:listar')
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/form_usuario.html', {'form': form, 'accion': 'Crear'})


@login_required
def editar_usuario(request, usuario_id):
    if not es_admin(request.user):
        messages.error(request, "No tienes permisos para editar usuarios.")
        return redirect('no_autorizado')

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('usuarios:listar')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/form_usuario.html', {'form': form, 'accion': 'Editar'})


@login_required
def eliminar_usuario(request, usuario_id):
    if not es_admin(request.user):
        messages.error(request, "No tienes permisos para eliminar usuarios.")
        return redirect('no_autorizado')

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('usuarios:listar')

    return render(request, 'usuarios/eliminar_confirmacion.html', {'usuario': usuario})

