from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=128)
    user_birthdate = models.DateField()


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')


class Order(models.Model):
    order_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_products = models.ManyToManyField(Product)
    order_datetime = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
