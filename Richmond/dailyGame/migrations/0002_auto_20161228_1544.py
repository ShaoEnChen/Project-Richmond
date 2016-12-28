# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 44, 33, 860001)),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 44, 33, 861493)),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 44, 33, 860836)),
        ),
    ]
