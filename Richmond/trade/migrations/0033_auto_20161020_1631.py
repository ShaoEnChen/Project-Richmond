# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0032_auto_20161020_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='cur_assets',
            field=models.FloatField(default=300000.0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 31, 42, 771074)),
        ),
    ]
