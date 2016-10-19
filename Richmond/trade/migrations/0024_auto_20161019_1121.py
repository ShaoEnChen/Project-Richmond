# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0023_auto_20161018_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 19, 11, 21, 20, 764414)),
        ),
    ]
