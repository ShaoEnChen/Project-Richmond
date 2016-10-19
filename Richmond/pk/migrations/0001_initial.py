# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PKGame',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('invitor', models.CharField(max_length=100)),
                ('invitee', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0, choices=[(0, '等待中'), (1, '進行中'), (2, '已結束'), (-1, '取消')])),
                ('mode', models.IntegerField(default=1, choices=[(1, '績效評比'), (2, '模式2')])),
            ],
        ),
    ]
