# Generated by Django 4.0.5 on 2022-07-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0003_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.permission'),
        ),
    ]
