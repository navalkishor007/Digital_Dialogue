# Generated by Django 3.1.3 on 2021-05-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_auto_20210504_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_users',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registered_users',
            name='user_phone',
            field=models.IntegerField(),
        ),
    ]
