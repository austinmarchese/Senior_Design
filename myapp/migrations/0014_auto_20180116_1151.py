# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20180116_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Austin', help_text='What is Your Name', max_length=50)),
                ('milk', models.CharField(default='No', help_text='Do you want Milk', max_length=50)),
                ('sugar', models.CharField(default='Yes', help_text='Do you want sugar', max_length=50)),
                ('run', models.IntegerField(default=1, help_text='Please Enter a Number')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
