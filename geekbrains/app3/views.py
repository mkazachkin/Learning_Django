from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render


class HelloView(View):
    @classmethod
    def get(cls, request, year, month, slug):
        return HttpResponse(f'Hello World from class!\nYear: {year}\nMonth: {month}\nSlug: {slug}')


class IndexView(View):
    @classmethod
    def get(cls, request):
        context = {'name': 'John'}
        return render(request, 'app3/index.html', context)
