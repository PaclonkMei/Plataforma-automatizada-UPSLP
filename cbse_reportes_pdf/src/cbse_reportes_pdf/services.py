from .exporters.pdf import reporte_a_pdf_bytes

def generar_pdf(payload: dict) -> bytes:
    """
    API del componente (CBSE):
    recibe datos normalizados y regresa PDF (bytes).
    """
    return reporte_a_pdf_bytes(payload)
