# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0075_auto_20161009_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cron_job_log',
            name='status_code',
            field=models.CharField(max_length=1, choices=[('1', 'cron_job_success'), ('2', 'cron_job_failed')]),
        ),
        migrations.AlterField(
            model_name='cron_job_log',
            name='title',
            field=models.CharField(max_length=48),
        ),
    ]
