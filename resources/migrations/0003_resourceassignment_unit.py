# Generated by Django 4.2.16 on 2024-11-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_dispatchrequest_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceassignment',
            name='unit',
            field=models.CharField(default='units', max_length=50),
        ),
    ]
