# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-05 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20170402_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='referrer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]