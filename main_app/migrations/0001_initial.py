# Generated by Django 2.2.9 on 2020-01-24 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('year_published', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('cart', models.ManyToManyField(to='main_app.Cart')),
            ],
        ),
    ]