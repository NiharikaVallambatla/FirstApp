# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-18 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home2Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing_list',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home2Home.persons'),
        ),
    ]
