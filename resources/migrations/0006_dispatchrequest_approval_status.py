# Generated by Django 4.2.16 on 2024-11-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_personnel_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchrequest',
            name='approval_status',
            field=models.CharField(choices=[('Pending', 'Đang xử lý'), ('Not approved', 'Không phê duyệt'), ('Approved', 'Đã phê duyệt')], default='Pending', max_length=50),
        ),
    ]
