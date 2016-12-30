# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0002_auto_20161228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkgame',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='pkgame',
            name='life',
            field=models.IntegerField(choices=[(1, '1週'), (2, '2週'), (3, '3週'), (4, '4週'), (5, '5週'), (6, '6週'), (7, '7週'), (8, '8週'), (0, '永久持續')], default=1),
        ),
        migrations.AlterField(
            model_name='pkgame',
            name='mode',
            field=models.IntegerField(choices=[(1, '績效評比'), (2, '資產評比')], default=1),
        ),
        migrations.AlterField(
            model_name='pkgame',
            name='status',
            field=models.IntegerField(choices=[(0, '等待中'), (1, '進行中'), (2, '已結束'), (-1, '已取消')], default=0),
        ),
    ]
