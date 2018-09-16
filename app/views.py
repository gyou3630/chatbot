from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def keyboard(request, service_id):
    return JsonResponse(
        {
            'type': 'text'
        }
    )


@csrf_exempt
def message(request, service_id):
    content = json.loads((request.body).decode('utf-8'))['content']
    text = '(/^0^)/'
    if service_id == 1:
        if content == '안녕':
            text = '안녕 오늘 기분어때?'
        elif '시험' in content and '긴장' in content:
            text = '그치 떨리겠다 그래도 긴장말고 시험 잘쳐'
    elif service_id == 2:
        if content == '안녕':
            text = '오늘 학교 시험이지?'
        elif '떨려' in content:
            text = '시험 잘칠거야 긴장하지말구!'
    elif service_id == 3:
        if content == '안녕':
            text = '오늘 중간고사지? 시험 잘쳐!!'
        elif '떨' in content:
            text = '잘칠거야 화이팅!!'
    elif service_id == 4:
        if content == '안녕':
            text = '오늘 중간고사지? 우리가 응원할께!!'
        elif '감동' in content:
            text = '우리가 응원해주니까 잘칠거야 걱정마!!'
    return JsonResponse(
        {
            'message': {
                'text': text
            }
        }
    )