# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0027_auto_20161004_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(verbose_name='cronjob_exec_time', default=datetime.datetime(2016, 10, 4, 18, 55, 51, 96788)),
        ),
    ]