# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0021_auto_20161020_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 8, 54, 7, 199211)),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 8, 54, 7, 201360)),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 8, 54, 7, 200495)),
        ),
    ]
