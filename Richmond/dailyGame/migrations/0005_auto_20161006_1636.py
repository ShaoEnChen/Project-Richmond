# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0004_auto_20161006_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 6, 16, 36, 17, 339195)),
        ),
    ]
