# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('surname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('phoneno', models.IntegerField()),
                ('emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]
