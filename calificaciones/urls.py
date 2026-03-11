from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'calificaciones'

urlpatterns = [
    # Registrar manualmente una calificación
    path('registrar/', views.registrar_calificacion, name='registrar_calificacion'),

    # Mensaje de éxito tras registrar
    path('exito/', views.calificacion_exitosa, name='calificacion_exitosa'),

    # Vista de no autorizado (del app calificaciones)
    path('no-autorizado/', views.no_autorizado, name='no_autorizado'),

    # Vista del alumno para ver sus calificaciones
    path('ver/', views.ver_calificaciones, name='ver_calificaciones'),

    # --- Subida de calificaciones desde archivo ---
    # Ruta corta bajo /calificaciones/
    path('subir/', views.subir_calificaciones, name='subir_calificaciones'),

    # Rutas pensadas para el rol profesor (más expresivas):
    path('profesor/subir/', views.subir_calificaciones, name='subir_calificaciones_profesor'),

    # Historial y estadísticas para profesor
    path('profesor/historial/', views.historial_profesor, name='historial_profesor'),
    path('profesor/historial/exportar/', views.exportar_historial_excel, name='exportar_historial'),

    # ✅ NUEVAS RUTAS: Editar y eliminar calificaciones
    path('profesor/editar/<int:calificacion_id>/', views.editar_calificacion, name='editar_calificacion'),
    path('profesor/eliminar/<int:calificacion_id>/', views.eliminar_calificacion, name='eliminar_calificacion'),

    # Índice para profesor -> redirige a subir
    path(
        'profesor/',
        RedirectView.as_view(pattern_name='calificaciones:subir_calificaciones_profesor', permanent=False),
        name='prof_calificaciones_index'
    ),
]