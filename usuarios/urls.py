
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.listar_usuarios, name='listar'),  # /usuarios/
    path('crear/', views.crear_usuario, name='crear'),  # /usuarios/crear/
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar'),  # /usuarios/editar/1/
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar'),  # /usuarios/eliminar/1/
]
