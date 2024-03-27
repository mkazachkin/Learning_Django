import logging

from django.http import HttpResponse
from random import choice


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world!')


def about(request):
    return HttpResponse('About us')


def coin(request):
    return HttpResponse(choice(['Выпал орёл', 'Выпала решка']))

def cube(request):
    return HttpResponse(choice([
        '<h1>⚀</h1>',
        '<h1>⚁</h1>',
        '<h1>⚂</h1>',
        '<h1>⚃</h1>',
        '<h1>⚄</h1>',
        '<h1>⚅</h1>'
    ]))
