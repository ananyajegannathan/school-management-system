# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20170530_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.Section'),
        ),
    ]