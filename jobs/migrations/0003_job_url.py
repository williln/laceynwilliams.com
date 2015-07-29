# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150728_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default=datetime.datetime(2015, 7, 29, 4, 21, 54, 75602, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
