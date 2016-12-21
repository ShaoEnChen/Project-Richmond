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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_type', models.IntegerField(default=0, choices=[(0, b'\xe7\xb3\xbb\xe7\xb5\xb1\xe9\x80\x9a\xe7\x9f\xa5'), (1, b'\xe8\xad\xa6\xe5\x91\x8a'), (2, b'\xe9\x82\x80\xe8\xab\x8b')])),
                ('n_from', models.CharField(default=b'system', max_length=100)),
                ('n_to', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 21, 10, 57, 1, 593581))),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
