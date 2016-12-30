# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0002_auto_20161228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='cron_job_log',
            name='status_code',
            field=models.CharField(choices=[('1', 'cron_job_success'), ('2', 'cron_job_failed')], max_length=1),
        ),
    ]
