# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-10-19 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=32)),
                ('super_number', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'admin_user',
            },
        ),
    ]
