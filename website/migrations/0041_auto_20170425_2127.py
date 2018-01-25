# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-25 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_auto_20170421_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='pockets',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='sub_profiles',
        ),
        migrations.AddField(
            model_name='merchant',
            name='default_pocket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merchant_profile_default_pocket', to='website.Pocket'),
        ),
    ]