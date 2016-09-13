# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('stock_id', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('end_price', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('total_num', models.IntegerField()),
                ('yesterday_end', models.FloatField()),
                ('start_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
            ],
        ),
    ]
