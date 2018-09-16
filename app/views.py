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


class TextFilter:
    def __init__(self, default_answer='Default'):
        self.filter_words_list = []
        self.default_answer = default_answer

    def add_filter(self, *args, answer=''):
        self.filter_words_list.append((args, answer))

    def run(self, sentence):
        for filter_words, answer in self.filter_words_list:
            for filter_word in filter_words:
                if filter_word in sentence:
                    return answer
        return self.default_answer


text_filters = [TextFilter() for i in range(4)]

text_filter_1 = text_filters[0]
text_filter_1.add_filter('안녕', answer='안녕 오늘 기분어때?')
text_filter_1.add_filter('시험', '긴장', answer='그치 떨리겠다ㅜ 그래도 긴장말고 시험 잘쳐ㅎㅎ')

text_filter_2 = text_filters[1]
text_filter_2.add_filter('안녕', answer='오늘 학교 시험이지?')
text_filter_2.add_filter('떨', answer='시험 잘칠거야ㅎㅎ 긴장하지말구!')

text_filter_3 = text_filters[2]
text_filter_3.add_filter('안녕', answer='오늘 중간고사지? 시험 잘쳐!!')
text_filter_3.add_filter('떨', answer='잘칠거야 화이팅!!')

text_filter_4 = text_filters[3]
text_filter_4.add_filter('안녕', answer='오늘 중간고사지? 우리가 응원할께!!')
text_filter_4.add_filter('감동', answer='우리가 응원해주니까 잘칠거야 걱정마!!')


@csrf_exempt
def message(request, service_id):
    content = json.loads(request.body.decode('utf-8'))['content']
    # text = '(/^0^)/~'
    text = text_filters[service_id - 1].run(content)
    return JsonResponse(
        {
            'message': {
                'text': text
            }
        }
    )