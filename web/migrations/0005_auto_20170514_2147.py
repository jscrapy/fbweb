# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-14 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170509_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qikan',
            name='feng_mian',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='封面'),
        ),
    ]
