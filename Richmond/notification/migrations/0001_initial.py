# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('n_type', models.IntegerField(choices=[(0, '系統通知'), (1, '警告'), (2, '邀請')], default=0)),
                ('n_from', models.CharField(max_length=100)),
                ('n_to', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 10, 18, 19, 58, 45, 748008))),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
