
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views import redireccion_por_rol, no_autorizado, bienvenida, inicio_publico

urlpatterns = [
    # Página pública
    path('', inicio_publico, name='inicio_publico'),

    # Admin de Django
    path('admin/', admin.site.urls),

    # ✅ Incluir rutas del app "usuarios" con namespace
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),

    # 🔗 Incluir rutas del app "calificaciones" BAJO prefijo /calificaciones/
    path('calificaciones/', include('calificaciones.urls')),

    # ✅ Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Redirección por rol y páginas varias
    path('inicio/', redireccion_por_rol, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('no_autorizado/', no_autorizado, name='no_autorizado'),
]
