# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='trade_company',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
