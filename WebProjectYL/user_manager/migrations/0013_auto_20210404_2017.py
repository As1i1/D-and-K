# Generated by Django 3.1.7 on 2021-04-04 15:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0012_auto_20210404_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 20, 17, 22, 878559), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='news',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='user_manager.news'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='repost',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='user_manager.repost'),
        ),
        migrations.AlterField(
            model_name='repost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 20, 17, 22, 879557), verbose_name='дата создания'),
        ),
    ]