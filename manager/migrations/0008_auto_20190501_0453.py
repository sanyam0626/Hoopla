# Generated by Django 2.0.6 on 2019-05-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20190423_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='user_address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user_landmark',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user_pincode',
            field=models.CharField(default='', max_length=30),
        ),
    ]
