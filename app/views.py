from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def keyboard(request):
    return JsonResponse(
        {
            'type': 'text'
        }
    )


@csrf_exempt
def message(request):
    print(' printing ==>', request.body)
    text = json.loads((request.body).decode('utf-8'))['text']
    return JsonResponse(
        {
            'text': text
        }
    )