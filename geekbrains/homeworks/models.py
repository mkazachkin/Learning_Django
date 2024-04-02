from django.db import models, connection


class Clients(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.TextField()
    registered_date = models.DateField()

    def __str__(self):
        return f'Client: {self.name}, email: {self.email}, phone: {self.phone}, registered: {self.registered_date}'


class Products(models.Model):
    name = models.CharField(max_length=128)
    descr = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    arrived_date = models.DateField()

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}, arrived: {self.arrived_date}'


class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_date = models.DateField()
