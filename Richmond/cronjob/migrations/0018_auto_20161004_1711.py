# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0017_auto_20161004_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron_job_log',
            name='exec_time',
            field=models.DateTimeField(verbose_name='cronjob_exec_time', default=datetime.datetime(2016, 10, 4, 17, 11, 45, 676178)),
        ),
    ]