# Generated by Django 2.0.4 on 2018-04-17 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avaliable',
            new_name='available',
        ),
    ]