# Generated by Django 3.2.6 on 2021-09-09 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_amount',
            new_name='amount_to_pay',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
    ]