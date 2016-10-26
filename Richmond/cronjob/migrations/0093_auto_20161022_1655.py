# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0092_auto_20161020_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 16, 55, 37, 60114)),
        ),
    ]
