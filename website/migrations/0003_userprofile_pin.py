# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-04 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170104_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pin',
            field=models.CharField(blank=True, default=b'0000', max_length=10, null=True),
        ),
    ]