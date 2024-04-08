import logging

from django.shortcuts import render
from .forms import UserForm, TestFields

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    logger.info('qq')
    return render(request, 'app4/user_form.html', {'form': form})


def test_fields(request):
    form = TestFields()
    return render(request, 'app4/user_form.html', {'form': form})
