# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyGame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='desc',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
