# Generated by Django 3.2.6 on 2021-09-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210907_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]