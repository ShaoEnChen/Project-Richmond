# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0025_auto_20161019_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 20, 3, 55, 59, 446602)),
        ),
    ]
