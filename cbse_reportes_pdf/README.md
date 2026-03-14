CBSE Reportes PDF
Este componente se encarga de la generación automatizada de reportes académicos en formato PDF para la Plataforma Automatizada UPSLP. Está diseñado como un paquete de Python instalable y reutilizable.

* Estructura del Proyecto 
La arquitectura sigue el estándar de la carpeta src para separar el código fuente de la configuración de empaquetado

* Instalación y Configuración
Para trabajar en este componente, asegúrate de tener el entorno virtual activo y las herramientas de construcción actualizadas, se debe de tener el modulo descomprimido directamente en la raiz del codigo antes de proceder con la instalación.

Actualizar herramientas de Pip:
Consola:
python -m pip install pip setuptools wheel

Dentro de la carpeta del modulo, ejecutar:
python -m pip install -e .

* Dependencias Principales
ReportLab (4.4.10+): Motor principal para la creación de los documentos PDF.

Pillow: Gestión de recursos gráficos e imágenes dentro de los reportes.

* Pruebas de Funcionamiento
Puedes verificar que el módulo esté correctamente instalado ejecutando este comando en la terminal:

PowerShell
python -c "from cbse_reportes_pdf.services import generar_pdf; print('Módulo cargado correctamente')"
Ejemplo de uso rápido:
Python
from cbse_reportes_pdf.services import generar_pdf

data = {
    'alumno': 'Juan Pérez',
    'filas': [{'materia': 'C++', 'calificacion': 95, 'fecha': '2026-03-13', 'profesor': 'Ing. García'}],
    'estadisticas': {'promedio': 95}
}

pdf_content = generar_pdf(data)
with open('reporte.pdf', 'wb') as f:
    f.write(pdf_content)