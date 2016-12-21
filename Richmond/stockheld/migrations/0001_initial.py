# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holding_Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=100)),
                ('s_id', models.CharField(max_length=10)),
                ('hstock', models.IntegerField(default=0)),
            ],
        ),
    ]
