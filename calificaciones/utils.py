from django.core.mail import send_mail
from django.conf import settings

def enviar_notificacion_alumno(calificacion):
    """
    Envía un correo al alumno notificando su calificación.
    """
    try:
        alumno = calificacion.alumno
        asunto = f'Nueva calificación registrada - {calificacion.materia}'
        
        mensaje = f"""
Hola {alumno.first_name or alumno.username},

Se ha registrado una nueva calificación para ti:

📚 Materia: {calificacion.materia}
📊 Calificación: {calificacion.nota}
📅 Fecha: {calificacion.fecha.strftime('%d/%m/%Y')}
👨‍🏫 Profesor: {calificacion.profesor.get_full_name() or calificacion.profesor.username}

{'✅ ¡Felicidades! Aprobaste.' if calificacion.nota >= 60 else '⚠️ Calificación reprobatoria.'}

---
Plataforma Académica Automatizada
        """
        
        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [alumno.email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False


def enviar_resumen_profesor(profesor, creados, actualizados, errores):
    """
    Envía un resumen al profesor después de importar calificaciones.
    """
    try:
        asunto = 'Resumen de importación de calificaciones'
        
        mensaje = f"""
Hola {profesor.first_name or profesor.username},

Tu importación de calificaciones ha finalizado:

📊 Resumen:
- ✅ Calificaciones creadas: {creados}
- 🔄 Calificaciones actualizadas: {actualizados}
- ❌ Errores encontrados: {errores}
- 📈 Total procesado: {creados + actualizados}

Puedes revisar el historial completo en la plataforma.

---
Plataforma Académica Automatizada
        """
        
        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [profesor.email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False