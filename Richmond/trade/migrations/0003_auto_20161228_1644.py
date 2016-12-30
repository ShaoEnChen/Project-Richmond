# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20161228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
