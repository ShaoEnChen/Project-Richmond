# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 44, 33, 852816)),
        ),
        migrations.AlterField(
            model_name='subscribelist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 44, 33, 853774)),
        ),
    ]
