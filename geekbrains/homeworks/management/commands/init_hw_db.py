import decimal
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from random import randint

from homeworks.models import Clients, Products, Orders


class Command(BaseCommand):
    CLIENTS_NUM = 99
    PRODUCTS_NUM = 99
    def handle(self, *args, **options):
        for i in range(50):
            client = Clients(
                name=f'Клиент_{i:02}',
                email=f'email_{i:02}@email.ru',
                phone=f'+7(999)000-00-{i:02}',
                address=f'Какая-то область, г. Какой-то, ул. Кого-то, д. {i}',
                registered_date=datetime.now() - timedelta(days=(self.CLIENTS_NUM - i)),
            )
            client.save()
            product = Products(
                name=f'Товар {i:02}',
                descr=f'Это замечательное описание товара {i:02}.\nВ нем несколько строк и есть "кавычки".',
                price=randint(1, 999) + 0.99,
                quantity=randint(1, 999),
                arrived_date=datetime.now() - timedelta(days=(self.PRODUCTS_NUM - i*3)),
            )
            product.save()
        client = Clients.objects.all()[1]
        days = 0
        for i in range(3):
            days = days * 6
            days += 1
            order = Orders(
                client=client,
                order_date=datetime.now() - timedelta(days=days + 1),
            )
            order.save()
            for j in range(randint(0, self.PRODUCTS_NUM)//5):
                product = Products.objects.order_by('?').first()
                order.products.add(product)
                order.total_price = decimal.Decimal(order.total_price) + product.price
            order.save()
