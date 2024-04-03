from django.http import HttpResponse
from django.views import View
from datetime import datetime, timedelta

from homeworks.models import Orders, Clients


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
