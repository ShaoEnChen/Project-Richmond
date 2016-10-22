# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0094_auto_20161020_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 31, 42, 781348)),
        ),
    ]
