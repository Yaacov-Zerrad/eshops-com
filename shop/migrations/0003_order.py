# Generated by Django 4.0.5 on 2022-07-02 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_category_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=127)),
                ('address', models.CharField(max_length=127)),
                ('city', models.CharField(max_length=127)),
                ('country', models.CharField(max_length=127)),
                ('zipcode', models.CharField(max_length=127)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
