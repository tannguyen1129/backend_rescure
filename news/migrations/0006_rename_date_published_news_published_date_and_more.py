# Generated by Django 4.2.16 on 2024-12-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_delete_disasternews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='date_published',
            new_name='published_date',
        ),
        migrations.RemoveField(
            model_name='news',
            name='link',
        ),
        migrations.RemoveField(
            model_name='news',
            name='region',
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(default='Nhân Dân', max_length=255),
        ),
    ]
