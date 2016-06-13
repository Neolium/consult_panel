# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 16:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import document_generator.models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0002_auto_20160512_1842'),
        ('document_generator', '0005_auto_20160613_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='profile',
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.CASCADE, to='consult_panel.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='template',
            name='document',
            field=models.FileField(
                max_length=500, upload_to=document_generator.models.upload_destination),
        ),
    ]
