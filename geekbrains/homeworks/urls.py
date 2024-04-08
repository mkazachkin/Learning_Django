from django.urls import path
from .views import OrdersView, ProductsView, ProductEditView

urlpatterns = [
    path('orders/', OrdersView.as_view(), name='Week orders'),
    path('orders/<int:days>/', OrdersView.as_view(), name='Week orders'),
    path('orders/<int:client_id>/<int:days>/', OrdersView.as_view(), name='Week orders'),
    path('products/', ProductsView.as_view(), name='Products view'),
    path('products/<int:page>/', ProductsView.as_view(), name='Products view'),
    path('product_edit/', ProductEditView.as_view(), name='Product edit view'),
    path('product_edit/<int:product_id>/', ProductEditView.as_view(), name='Product edit view'),
]
