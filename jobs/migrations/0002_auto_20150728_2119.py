# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='still_working',
            field=models.BooleanField(default=datetime.datetime(2015, 7, 29, 4, 19, 4, 615755, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
