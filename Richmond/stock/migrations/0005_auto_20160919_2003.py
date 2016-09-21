# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20160919_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='total_num',
            field=models.CharField(max_length=10),
        ),
    ]
