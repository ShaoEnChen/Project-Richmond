# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20160929_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
