# Generated by Django 4.0.5 on 2022-07-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_cart_qte'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='qte',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
