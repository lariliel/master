# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-03 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cybergoose', '0002_auto_20171112_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atmosphere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pAtm', models.FloatField(default=0)),
                ('TAtm', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='substance',
            name='QHeat',
            field=models.FloatField(default=0),
        ),
    ]