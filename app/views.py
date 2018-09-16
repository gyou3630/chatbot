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
    content = json.loads((request.body).decode('utf-8'))['content']
    if content == '안녕':
        text = '안녕 오늘 기분어때?'
    elif '시험' in content and '긴장' in content:
        text = '그치 떨리겠다 그래도 긴장말고 시험 잘쳐'
    else:
        text = '(/^0^)/'
    return JsonResponse(
        {
            'message': {
                'text': text
            }
        }
    )