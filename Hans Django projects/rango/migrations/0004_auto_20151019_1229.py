# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_category_pipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pipo',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 10, 19)),
            preserve_default=True,
        ),
    ]
