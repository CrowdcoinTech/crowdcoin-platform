# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-06 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20170106_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2017, 1, 6, 18, 54, 50, 231903)),
        ),
    ]