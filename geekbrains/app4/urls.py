from django.urls import path
from .views import user_form, test_fields

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('test/', test_fields, name='test_form'),
]
