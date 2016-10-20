# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0003_auto_20161020_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkgame',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 5, 48, 35, 75895)),
        ),
    ]
