# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0002_auto_20170827_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posthaber',
            options={'ordering': ['-created_at'], 'verbose_name': 'Haber', 'verbose_name_plural': 'Haberler'},
        ),
    ]
