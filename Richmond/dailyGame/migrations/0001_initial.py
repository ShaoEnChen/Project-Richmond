# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50, default='')),
                ('desc', models.CharField(max_length=200, default='')),
                ('cost', models.FloatField(default=10000.0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
