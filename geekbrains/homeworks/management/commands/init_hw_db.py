import decimal
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand


from homeworks.models import Clients, Products, Orders


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(5):
            client = Clients(
                name=f'Клиент_{i}',
                email=f'email_{i}@email.ru',
                phone=f'+7(999)000-00-0{i}',
                address=f'Какая-то область, г. Какой-то, ул. Кого-то, д. {i}',
                registered_date=datetime.now() - timedelta(days=(10 - i)),
            )
            client.save()
            product = Products(
                name=f'Товар {i}',
                descr=f'Это замечательное описание товара {i}.\nВ нем несколько строк и есть "кавычки".',
                price=99.99 - i,
                quantity=100 - i,
                arrived_date=datetime.now() - timedelta(days=(100 - i*3)),
            )
            product.save()
        client = Clients.objects.filter(name='Клиент_3')[0]
        order = Orders(
            client=client,
            order_date=datetime.now()
        )
        order.save()
        products = Products.objects.all()
        for i in range(5):
            order.products.add(products[i])
            order.total_price = decimal.Decimal(order.total_price) + products[i].price
        order.save()
