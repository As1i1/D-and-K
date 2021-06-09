# Generated by Django 3.1.7 on 2021-05-26 16:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_manager.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_manager', '0033_auto_20210526_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityPostFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=user_manager.models.community_post_directory)),
                ('c_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='user_manager.communitypost')),
            ],
            options={
                'verbose_name': 'Файл новости',
                'verbose_name_plural': 'Файлы новостей',
            },
        ),
    ]
