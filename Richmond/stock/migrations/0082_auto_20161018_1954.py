# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0081_auto_20161018_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 18, 19, 54, 22, 743898)),
        ),
    ]