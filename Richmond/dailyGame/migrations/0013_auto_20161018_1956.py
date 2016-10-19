# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0012_auto_20161018_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 18, 19, 56, 52, 243135)),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 18, 19, 56, 52, 244885)),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 18, 19, 56, 52, 243961)),
        ),
    ]
