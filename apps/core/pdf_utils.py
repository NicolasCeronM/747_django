from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def generar_factura_pdf(order):
    template = get_template('pdf/factura.html')  # HTML del PDF
    html = template.render({'order': order})
    resultado = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), resultado)
    if not pdf.err:
        return resultado.getvalue()
    return None