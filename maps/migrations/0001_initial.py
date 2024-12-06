# Generated by Django 4.2.16 on 2024-12-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisasterZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('radius', models.FloatField()),
                ('disaster_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]