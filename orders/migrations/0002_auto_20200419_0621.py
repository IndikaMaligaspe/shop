# Generated by Django 2.0.5 on 2020-04-19 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]