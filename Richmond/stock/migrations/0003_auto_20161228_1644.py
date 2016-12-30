# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20161228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
