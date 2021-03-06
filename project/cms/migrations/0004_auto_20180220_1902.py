# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('executors', '0002_auto_20180220_1808'),
        ('cms', '0003_auto_20180217_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='short_desc',
        ),
        migrations.RemoveField(
            model_name='task',
            name='short_desc',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='short_desc',
        ),
        migrations.AddField(
            model_name='course',
            name='executors',
            field=models.ManyToManyField(to='executors.Executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='Текст задания'),
        ),
    ]
