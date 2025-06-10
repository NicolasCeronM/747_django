from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .pdf_utils import generar_factura_pdf

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