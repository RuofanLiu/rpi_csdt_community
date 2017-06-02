# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-07 23:11
from __future__ import unicode_literals

import datetime

import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0014_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileupload',
            old_name='f',
            new_name='file_path',
        ),
        migrations.AlterField(
            model_name='approval',
            name='when_requested',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='when_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='project',
            name='when_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 4, 7, 23, 11, 32, 148019, tzinfo=utc), verbose_name=b'Created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='when_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 4, 7, 23, 11, 38, 903639, tzinfo=utc), verbose_name=b'Last Changed'),
            preserve_default=False,
        ),
    ]