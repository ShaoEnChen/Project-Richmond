# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0009_auto_20161020_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 15, 9, 596169)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='n_from',
            field=models.CharField(default='system', max_length=100),
        ),
    ]
