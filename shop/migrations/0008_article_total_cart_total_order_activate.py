# Generated by Django 4.0.5 on 2022-07-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_delete_articleuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='activate',
            field=models.BooleanField(default=True),
        ),
    ]
