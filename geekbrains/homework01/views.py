import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Homework 01 index page accessed')
    html_str = '''<!DOCTYPE html>
<html lang="ru">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homework 01</title>
</head>

<body>
    <div class="header">
        <h1>Это главная страница</h1>
    </div>
    <div class="content">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <div class="footer">

    </div>
</body>
    '''
    return HttpResponse(html_str)


def about(request):
    logger.info('Homework 02 about page accessed')
    html_str = '''<!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Homework 01</title>
    </head>

    <body>
        <div class="header">
            <h1>Это страница обо мне</h1>
        </div>
        <div class="content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
        <div class="footer">

        </div>
    </body>
    '''
    return HttpResponse(html_str)
