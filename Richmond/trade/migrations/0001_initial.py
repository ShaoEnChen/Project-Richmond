# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=100)),
                ('trade', models.CharField(max_length=1)),
                ('trade_company', models.CharField(max_length=5)),
                ('trade_num', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 10, 4, 20, 13, 48, 366580))),
            ],
        ),
    ]
