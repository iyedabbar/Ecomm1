# Generated by Django 3.2.6 on 2021-08-26 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='prod_img/')),
                ('slug', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '1. Products',
            },
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
            options={
                'verbose_name_plural': '2. ProductAttributes',
            },
        ),
    ]
