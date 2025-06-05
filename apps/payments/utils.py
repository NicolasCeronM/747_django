from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def enviar_correo_compra(usuario, pedido):
    asunto = f'🧾 Compra #{pedido.id} confirmada en SEVEN FOUR SEVEN'
    mensaje_html = render_to_string('email/confirmacion_compra.html', {
        'usuario': usuario,
        'pedido': pedido
    })

    email = EmailMessage(
        asunto,
        mensaje_html,
        settings.DEFAULT_FROM_EMAIL,
        [usuario.email],
    )
    email.content_subtype = 'html'

    pdf = generar_factura_pdf(pedido)
    if pdf:
        email.attach(f'factura_{pedido.id}.pdf', pdf, 'application/pdf')

    email.send(fail_silently=False)


def generar_factura_pdf(order):
    template = get_template('pdf/factura.html')  # HTML del PDF
    html = template.render({'order': order})
    resultado = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), resultado)
    if not pdf.err:
        return resultado.getvalue()
    return None
