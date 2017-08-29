# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-27 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogoCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='home-images')),
                ('title', models.CharField(max_length=250, null=True)),
                ('link1', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RightBannerBottom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='home-images')),
                ('title', models.CharField(max_length=250)),
                ('link1', models.CharField(max_length=250)),
                ('link1_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RightBannerTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='home-images')),
                ('title', models.CharField(max_length=250)),
                ('link1', models.CharField(max_length=250)),
                ('link1_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='home-images')),
                ('title', models.CharField(max_length=250)),
                ('link1', models.CharField(max_length=250)),
                ('link1_title', models.CharField(max_length=25)),
            ],
        ),
    ]
