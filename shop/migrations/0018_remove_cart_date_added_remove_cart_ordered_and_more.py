# Generated by Django 4.0.5 on 2022-07-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_order_num_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.AddField(
            model_name='article',
            name='date_order',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
