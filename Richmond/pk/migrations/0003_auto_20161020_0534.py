# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pk', '0002_auto_20161020_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkgame',
            name='invitee_init_assets',
            field=models.FloatField(editable=False, default=300000.0),
        ),
        migrations.AddField(
            model_name='pkgame',
            name='invitor_init_assets',
            field=models.FloatField(editable=False, default=300000.0),
        ),
    ]
