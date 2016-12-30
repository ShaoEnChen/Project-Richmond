# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20161228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='n_from',
            field=models.CharField(max_length=100, default='system'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='n_type',
            field=models.IntegerField(choices=[(0, '系統通知'), (1, '警告'), (2, '邀請')], default=0),
        ),
    ]
