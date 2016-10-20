# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pkgame',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, '等待中'), (1, '進行中'), (2, '已結束'), (-1, '已取消')]),
        ),
    ]
