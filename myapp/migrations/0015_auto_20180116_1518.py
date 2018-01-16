# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20180116_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='What is Your Name ', max_length=50)),
                ('milk', models.CharField(help_text='Do you want Milk (Yes or No)', max_length=50)),
                ('sugar', models.CharField(help_text='Do you want sugar (Yes or No)', max_length=50)),
                ('run', models.IntegerField(help_text='Please Enter a Number')),
            ],
        ),
        migrations.DeleteModel(
            name='Mode',
        ),
    ]
