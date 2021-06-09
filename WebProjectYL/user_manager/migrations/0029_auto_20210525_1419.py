# Generated by Django 3.1.7 on 2021-05-25 09:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_manager.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_manager', '0028_auto_20210420_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, null=True, verbose_name='Название сообщества')),
                ('describe', models.TextField(max_length=1000, null=True, verbose_name='Описание сообщества')),
                ('avatar', models.FileField(blank=True, null=True, upload_to=user_manager.models.community_avatar_directory)),
                ('admins', models.ManyToManyField(related_name='communities_admin', to=settings.AUTH_USER_MODEL, verbose_name='Админы')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='communities_creator')),
                ('members', models.ManyToManyField(related_name='communities', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики')),
            ],
            options={
                'verbose_name': 'Сообщество',
                'verbose_name_plural': 'Сообщества',
            },
        ),
        migrations.AlterModelOptions(
            name='newsfile',
            options={'verbose_name': 'Файл новости', 'verbose_name_plural': 'Файлы новостей'},
        ),
        migrations.CreateModel(
            name='CommunityPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField(max_length=1000, verbose_name='Контент')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата создания')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='user_manager.community')),
            ],
            options={
                'verbose_name': 'Новость сообщества',
                'verbose_name_plural': 'Новости сообществ',
            },
        ),
    ]