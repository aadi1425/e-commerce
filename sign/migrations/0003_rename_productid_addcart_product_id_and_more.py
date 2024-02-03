# Generated by Django 5.0 on 2024-01-23 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_addcart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcart',
            old_name='productid',
            new_name='product_id',
        ),
        migrations.AlterModelTable(
            name='addcart',
            table=None,
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('f_name', models.CharField(max_length=4544)),
                ('l_name', models.CharField(max_length=544)),
                ('username', models.CharField(max_length=7888)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('EUROPE', 'EUROPE'), ('CANADA', 'CANADA'), ('other', 'other')], max_length=646)),
                ('state', models.CharField(choices=[('Ahmedabad', 'Ahmedabad'), ('New York', 'New York'), ('London', 'London'), ('Toronto', 'Toronto'), ('other', 'other')], max_length=5454)),
                ('zip', models.IntegerField()),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sign.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sign.checkout')),
                ('prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.product')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
