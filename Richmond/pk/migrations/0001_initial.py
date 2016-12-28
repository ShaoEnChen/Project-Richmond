# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PKGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invitor', models.CharField(max_length=100)),
                ('invitee', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 562297))),
                ('invitor_init_assets', models.FloatField(default=300000.0, editable=False)),
                ('invitee_init_assets', models.FloatField(default=300000.0, editable=False)),
                ('status', models.IntegerField(default=0, choices=[(0, b'\xe7\xad\x89\xe5\xbe\x85\xe4\xb8\xad'), (1, b'\xe9\x80\xb2\xe8\xa1\x8c\xe4\xb8\xad'), (2, b'\xe5\xb7\xb2\xe7\xb5\x90\xe6\x9d\x9f'), (-1, b'\xe5\xb7\xb2\xe5\x8f\x96\xe6\xb6\x88')])),
                ('life', models.IntegerField(default=1, choices=[(1, b'1\xe9\x80\xb1'), (2, b'2\xe9\x80\xb1'), (3, b'3\xe9\x80\xb1'), (4, b'4\xe9\x80\xb1'), (5, b'5\xe9\x80\xb1'), (6, b'6\xe9\x80\xb1'), (7, b'7\xe9\x80\xb1'), (8, b'8\xe9\x80\xb1'), (0, b'\xe6\xb0\xb8\xe4\xb9\x85\xe6\x8c\x81\xe7\xba\x8c')])),
                ('mode', models.IntegerField(default=1, choices=[(1, b'\xe7\xb8\xbe\xe6\x95\x88\xe8\xa9\x95\xe6\xaf\x94'), (2, b'\xe8\xb3\x87\xe7\x94\xa2\xe8\xa9\x95\xe6\xaf\x94')])),
            ],
        ),
    ]
