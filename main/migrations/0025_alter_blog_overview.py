# Generated by Django 3.2.6 on 2021-09-13 18:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
