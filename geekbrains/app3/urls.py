from django.urls import path
from .views import HelloView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('<int:year>/', HelloView.as_view(), name='Hello view'),
    path('<int:year>/<int:month>/<slug:slug>/', HelloView.as_view(), name='Hello view 2'),
]
