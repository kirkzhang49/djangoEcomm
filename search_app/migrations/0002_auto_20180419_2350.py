# Generated by Django 2.0.4 on 2018-04-19 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
