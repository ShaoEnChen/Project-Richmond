# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_profile_is_in_daily_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('cost', models.FloatField(default=10000.0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_buy', models.BooleanField(default=True)),
                ('trade_num', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 10, 5, 17, 22, 46, 993617))),
                ('player', models.ForeignKey(to='players.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='JoinedPlayer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('init_assets', models.FloatField(editable=False, default=300000.0)),
                ('player', models.OneToOneField(to='players.Profile')),
            ],
        ),
    ]
