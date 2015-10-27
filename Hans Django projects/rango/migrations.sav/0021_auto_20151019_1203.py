# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0020_auto_20151019_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug2',
            field=models.SlugField(default=datetime.date(2015, 10, 19), unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.IntegerField(default=0),
        ),
    ]
