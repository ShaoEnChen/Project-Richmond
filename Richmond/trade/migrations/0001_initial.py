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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=100)),
                ('cur_assets', models.FloatField(default=300000.0)),
                ('is_buy', models.BooleanField(default=True)),
                ('trade_company', models.CharField(max_length=5)),
                ('trade_num', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 546141))),
            ],
        ),
    ]
