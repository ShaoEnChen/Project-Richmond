# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0006_auto_20161020_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkgame',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 16, 15, 9, 598017)),
        ),
    ]
