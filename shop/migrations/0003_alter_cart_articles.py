# Generated by Django 4.0.5 on 2022-07-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_article_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='articles',
            field=models.ManyToManyField(to='shop.article'),
        ),
    ]