# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-17 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'Python 3.6'), (1, 'Test 1'), (2, 'Test 2')], max_length=255, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Исполнитель кода',
                'verbose_name_plural': 'Исполнители кода',
            },
        ),
    ]
