from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Subscriber

# Create your views here.


@csrf_exempt
def guardar_correo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            accepted = data.get('accepted')

            if not email or not accepted:
                return JsonResponse({'success': False, 'error': 'Datos incompletos'})

            # Verificar si ya está registrado
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'error': 'Ya estás registrado'})

            Subscriber.objects.create(email=email, accepted_terms=accepted)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Método no permitido'})
