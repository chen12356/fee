# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-21 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0007_auto_20191021_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='recommender_id',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
