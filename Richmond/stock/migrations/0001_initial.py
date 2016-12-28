# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.CharField(max_length=10)),
                ('time', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 552462))),
                ('end_price', models.CharField(max_length=10)),
                ('buy_price', models.CharField(max_length=10)),
                ('sell_price', models.CharField(max_length=10)),
                ('total_num', models.CharField(max_length=10)),
                ('yesterday_end', models.CharField(max_length=10)),
                ('start_price', models.CharField(max_length=10)),
                ('high_price', models.CharField(max_length=10)),
                ('low_price', models.CharField(max_length=10)),
            ],
        ),
    ]
