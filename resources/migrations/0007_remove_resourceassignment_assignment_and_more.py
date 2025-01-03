# Generated by Django 4.2.16 on 2024-12-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_dispatchrequest_approval_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceassignment',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='resourceassignment',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='assigned_personnel',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='assigned_resources',
        ),
        migrations.DeleteModel(
            name='PersonnelAssignment',
        ),
        migrations.DeleteModel(
            name='ResourceAssignment',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_personnel',
            field=models.JSONField(default=list, help_text="Danh sách nhân sự: [{'personnel_id': ID, 'role': VAI_TRÒ, 'quantity': SỐ_LƯỢNG}]"),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_resources',
            field=models.JSONField(default=list, help_text="Danh sách tài nguyên: [{'resource_id': ID, 'quantity': SỐ_LƯỢNG, 'unit': ĐƠN_VỊ}]"),
        ),
    ]
