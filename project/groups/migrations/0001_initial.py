# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import project.modules.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название группы', max_length=64, verbose_name='Название')),
                ('progress', project.modules.fields.JSONField(blank=True, null=True)),
                ('members', models.ManyToManyField(related_name='membership', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
