# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cost',
            field=models.FloatField(default=10000.0),
        ),
    ]
