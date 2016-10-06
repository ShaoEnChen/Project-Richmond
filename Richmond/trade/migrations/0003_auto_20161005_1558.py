# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20161004_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='trade',
        ),
        migrations.AddField(
            model_name='trade',
            name='is_buy',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 5, 15, 58, 22, 492873)),
        ),
    ]
