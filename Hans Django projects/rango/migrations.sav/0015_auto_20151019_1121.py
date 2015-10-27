# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0014_auto_20151019_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug2',
            new_name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='pipo',
        ),
    ]
