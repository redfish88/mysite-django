# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_answer',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
