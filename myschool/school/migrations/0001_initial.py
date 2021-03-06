# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('std', models.CharField(default='DEFAULT VALUE', max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('father_name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=50, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='school.Teacher')),
                ('no_of_students', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='class_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
    ]
