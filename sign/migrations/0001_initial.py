# Generated by Django 5.0 on 2024-01-04 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=852)),
                ('image', models.ImageField(upload_to='upload/')),
                ('brand', models.CharField(max_length=8963)),
                ('color', models.CharField(max_length=52)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('des', models.CharField(max_length=5656)),
                ('price', models.IntegerField()),
                ('date_of_submit', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6664)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
