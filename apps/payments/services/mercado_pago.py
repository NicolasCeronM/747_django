import mercadopago
from django.conf import settings

sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)

def crear_preferencia(productos, back_urls):
    preference_data = {
        "items": productos,
        "back_urls": back_urls,
        "auto_return": "approved",
    }

    result = sdk.preference().create(preference_data)
    return result["response"]
