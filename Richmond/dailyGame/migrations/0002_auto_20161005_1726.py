# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinedplayer',
            name='id',
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 5, 17, 26, 7, 459299)),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='player',
            field=models.OneToOneField(primary_key=True, to='players.Profile', serialize=False),
        ),
    ]
