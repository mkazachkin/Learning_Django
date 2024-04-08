from django.forms import ModelForm

from .models import Products


class EditProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'descr', 'price', 'quantity', 'arrived_date', 'image']
