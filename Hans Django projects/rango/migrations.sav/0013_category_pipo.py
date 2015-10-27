# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pipo',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
