from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(AddCart)
admin.site.register(Checkout)
admin.site.register(OrderItem)