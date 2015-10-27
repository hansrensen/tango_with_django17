# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20151019_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pipo',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 10, 19), unique=True),
        ),
    ]
