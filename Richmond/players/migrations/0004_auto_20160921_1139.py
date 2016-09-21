# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20160912_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='assets',
            field=models.FloatField(default=300000.0),
        ),
    ]
