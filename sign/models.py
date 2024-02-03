from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=852)
    image = models.ImageField(upload_to='upload/')
    brand = models.CharField(max_length=8963)
    color = models.CharField(max_length=52)
    height = models.IntegerField()
    weight = models.IntegerField()
    des=models.CharField(max_length=5656)
    price= models.IntegerField()
    date_of_submit = models.DateField()


class Meta:
    db_table='Product'

class register(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField()
    gender=models.CharField(max_length=6664)
    contact=models.IntegerField()
    address=models.TextField()

class Meta:
    db_table='Register'

class AddCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product_id=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    qty=models.IntegerField()
    total=models.IntegerField()
    # gtotal=models.IntegerField()

class Meta:
    db_table="AddCart"

class Checkout(models.Model):
    country_choices = [
        ('India', 'India'),
        ('USA', 'USA'),
        ('EUROPE', 'EUROPE'),
        ('CANADA', 'CANADA'),
        ('other', 'other')
    ]
    state_Choices = [
        ('Ahmedabad', 'Ahmedabad'),
        ('New York', 'New York'),
        ('London', 'London'),
        ('Toronto', 'Toronto'),
        ('other', 'other')
    ]
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    # total_price = models.IntegerField()
    f_name = models.CharField(max_length=4544)
    l_name = models.CharField(max_length=544)
    username = models.CharField(max_length=7888)
    email=models.EmailField()
    address = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(choices=country_choices, max_length=646)
    state = models.CharField(choices=state_Choices, max_length=5454)
    zip = models.IntegerField()

class Meta:
    db_table='CheckOut'


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    order = models.ForeignKey(Checkout, on_delete=models.CASCADE, default=1)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img")
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    total_price = models.IntegerField()

class Meta:
    db_table='OrderItem'