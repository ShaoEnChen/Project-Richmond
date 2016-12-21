# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('cost', models.FloatField(default=10000.0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 21, 10, 57, 1, 590012))),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_buy', models.BooleanField(default=True)),
                ('trade_num', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 21, 10, 57, 1, 591959))),
            ],
        ),
        migrations.CreateModel(
            name='JoinedPlayer',
            fields=[
                ('player', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 12, 21, 10, 57, 1, 591092))),
                ('init_assets', models.FloatField(default=300000.0, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='gamerecord',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
