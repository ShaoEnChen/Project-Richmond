# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_in_daily_game',
            field=models.BooleanField(default=False),
        ),
    ]
