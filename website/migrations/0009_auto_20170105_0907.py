# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-05 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20170105_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirtimePaymentLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('identifiers', models.ManyToManyField(blank=True, to='website.UniqueIdentifier')),
            ],
        ),
        migrations.AlterField(
            model_name='pocket',
            name='identifiers',
            field=models.ManyToManyField(blank=True, to='website.UniqueIdentifier'),
        ),
        migrations.AlterField(
            model_name='pocket',
            name='transactions',
            field=models.ManyToManyField(blank=True, to='website.Transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='identifiers',
            field=models.ManyToManyField(blank=True, to='website.UniqueIdentifier'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='identifier',
            field=models.ManyToManyField(blank=True, to='website.UniqueIdentifier'),
        ),
        migrations.AddField(
            model_name='airtimepaymentlead',
            name='pocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airtime_payment_lead_pocket', to='website.Pocket'),
        ),
        migrations.AddField(
            model_name='airtimepaymentlead',
            name='sim_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.SimCard'),
        ),
    ]