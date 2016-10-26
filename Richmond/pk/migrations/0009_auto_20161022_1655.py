# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0008_auto_20161020_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkgame',
            name='life',
            field=models.IntegerField(choices=[(1, '1週'), (2, '2週'), (3, '3週'), (4, '4週'), (5, '5週'), (6, '6週'), (7, '7週'), (8, '8週'), (0, '永久持續')], default=1),
        ),
        migrations.AlterField(
            model_name='pkgame',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 16, 55, 37, 86887)),
        ),
    ]
