# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-18 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nikki', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='thing_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('person', models.CharField(max_length=255)),
                ('fromHome', models.BooleanField(default=True)),
            ],
        ),
    ]
