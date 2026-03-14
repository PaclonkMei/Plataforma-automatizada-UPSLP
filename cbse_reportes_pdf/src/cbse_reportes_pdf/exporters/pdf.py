# reportes/exporters/pdf.py
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def reporte_a_pdf_bytes(payload: dict) -> bytes:
    alumno = payload.get("alumno", "Alumno")
    filas = payload.get("filas", [])
    stats = payload.get("estadisticas", {})

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Reporte de {alumno}")
    y -= 25

    c.setFont("Helvetica", 11)
    c.drawString(50, y, "Estadísticas:")
    y -= 18
    for label, key in [("Total","total"), ("Promedio","promedio"), ("Máxima","maxima"), ("Mínima","minima")]:
        c.drawString(60, y, f"- {label}: {stats.get(key)}")
        y -= 14
    y -= 10

    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Detalle:")
    y -= 18

    c.setFont("Helvetica", 10)
    for r in filas:
        linea = f"{r.get('materia','')} | {r.get('calificacion','')} | {r.get('fecha','')} | {r.get('profesor','')}"
        c.drawString(60, y, linea[:110])
        y -= 13
        if y < 60:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 10)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()
