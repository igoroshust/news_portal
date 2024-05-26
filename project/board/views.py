from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .tasks import news_created # hello, weekly_newsletter

class IndexView(View):
    def get(self, request):
        return HttpResponse('Письмо отправлено на почту')