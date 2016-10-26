# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0023_auto_20161020_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 16, 55, 37, 57595)),
        ),
    ]
