# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0002_auto_20161005_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 6, 16, 13, 14, 727877)),
        ),
        migrations.AlterField(
            model_name='gamerecord',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='joinedplayer',
            name='player',
            field=models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
