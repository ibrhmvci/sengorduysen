# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170828_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialIcons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Sosyal Medya Hesap Adı')),
                ('link', models.CharField(max_length=250, null=True, verbose_name='Sosyal Medya Hesap Adresi')),
            ],
            options={
                'verbose_name': ' Sosyal Medya Hesabı',
                'verbose_name_plural': 'Sosyal Medya Hesapları',
            },
        ),
    ]
