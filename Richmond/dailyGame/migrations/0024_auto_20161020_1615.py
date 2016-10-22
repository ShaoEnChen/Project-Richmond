# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0023_auto_20161020_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 15, 9, 593887)),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 15, 9, 595111)),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 15, 9, 594514)),
        ),
    ]
