# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_publication_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='slides',
            field=models.URLField(default=datetime.datetime(2015, 7, 30, 0, 0, 0, 779803, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='video',
            field=models.URLField(default=datetime.datetime(2015, 7, 30, 0, 0, 11, 268739, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
