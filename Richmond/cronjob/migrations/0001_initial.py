# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cron_Job_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=48)),
                ('exec_time', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 550513))),
                ('status_code', models.CharField(max_length=1, choices=[(b'1', 'cron_job_success'), (b'2', 'cron_job_failed')])),
            ],
        ),
    ]
