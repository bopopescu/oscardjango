# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_auto_20160107_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='partneraddress',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Company Name'),
        ),
    ]