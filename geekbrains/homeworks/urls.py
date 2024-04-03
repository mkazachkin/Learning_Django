from django.urls import path
from .views import OrdersView

urlpatterns = [
    path('orders/', OrdersView.as_view(), name='Week orders'),
    path('orders/<int:days>/', OrdersView.as_view(), name='Week orders'),
    path('orders/<int:client_id>/<int:days>/', OrdersView.as_view(), name='Week orders'),
]
