# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-03 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cybergoose', '0003_auto_20171203_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='substance',
            old_name='Q',
            new_name='QCond',
        ),
    ]