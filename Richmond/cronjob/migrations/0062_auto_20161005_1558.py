# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0061_auto_20161004_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 5, 15, 58, 22, 496185), verbose_name='cronjob_exec_time'),
        ),
    ]
