# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20160913_1747'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='Stock',
        ),
    ]
