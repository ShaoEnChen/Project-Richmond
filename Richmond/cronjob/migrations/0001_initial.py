# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cron_Job_Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=48, default='', verbose_name='cronjob_title')),
                ('exec_time', models.DateTimeField(auto_now_add=True, verbose_name='cronjob_exec_time')),
                ('status_code', models.CharField(max_length=1, choices=[('1', 'cron_job_success'), ('2', 'cron_job_failed')], default='1', verbose_name='cronjob_status')),
            ],
        ),
    ]
