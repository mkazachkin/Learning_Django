import logging

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from datetime import datetime, timedelta

from homeworks.forms import EditProductForm
from homeworks.models import Orders, Clients, Products


logger = logging.getLogger(__name__)


class OrdersView(View):
    @classmethod
    def get(cls, request, client_id=-1, days=7):
        start_date = datetime.now() - timedelta(days=days)
        end_date = datetime.now()
        if client_id > 0:
            client = Clients.objects.filter(id=client_id).first()
            orders = Orders.objects.filter(
                client=client,
                order_date__range=(start_date, end_date)
            ).order_by('order_date')
        else:
            orders = Orders.objects.filter(
                order_date__range=(start_date, end_date)
            ).order_by('order_date')
        result = ''
        for order in orders:
            result += f'\n{str(order)}'
        return HttpResponse(result.replace('\n', '<br>'))


class ProductsView(TemplateView):
    template_name = 'homeworks/products.html'
    PAGE_LIMIT = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = kwargs.get('page', 1)
        products = Products.objects.all().order_by('id')[
            page * self.PAGE_LIMIT - self.PAGE_LIMIT:page * self.PAGE_LIMIT
        ]
        context['products'] = products
        context['page'] = page
        return context


class ProductEditView(TemplateView):
    template_name = 'homeworks/product_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs.get('product_id', None)
        try:
            context['form'] = EditProductForm(
                instance=Products.objects.filter(id=product_id)[0]
            )
        except IndexError:
            context['form'] = EditProductForm()
        return context

    def post(self, request, **kwargs):
        form = EditProductForm(request.POST, request.FILES)
        context = self.get_context_data()
        context['form'] = form
        context['message'] = 'При загрузке формы произошла ошибка.'
        if context['form'].is_valid():
            product_id = kwargs.get('product_id', None)
            name = form.cleaned_data['name']
            descr = form.cleaned_data['descr']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            arrived_date = form.cleaned_data['arrived_date']
            if product_id:
                try:
                    Products.objects.filter(pk=product_id).update(
                        name=name,
                        descr=descr,
                        price=price,
                        quantity=quantity,
                        arrived_date=arrived_date,
                    )
                except Exception:
                    product_id = None
            if not product_id:
                product = Products(
                    name=name,
                    descr=descr,
                    price=price,
                    quantity=quantity,
                    arrived_date=arrived_date,
                )
                product.save()
                product_id = product.pk
            image = form.cleaned_data['image']
            if image:
                Products.objects.get(pk=product_id).image.delete(save=True)

                file_extension = image.name.split('.')[-1]
                file_name = f'{product_id}.{file_extension}'

                fs = FileSystemStorage()
                image.name = file_name
                fs.save(file_name, image)
                Products.objects.filter(pk=product_id).update(image=image)
            context['message'] = 'Загрузка формы успешно завершена.'
        return render(request, self.template_name, context=context)
