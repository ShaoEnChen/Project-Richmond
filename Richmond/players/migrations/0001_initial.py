# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 548030))),
                ('assets', models.FloatField(default=300000.0)),
                ('exp', models.IntegerField(default=0)),
                ('is_in_daily_game', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribeList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscriber', models.CharField(max_length=100)),
                ('subscribee', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 28, 15, 43, 56, 548978))),
            ],
        ),
    ]
