# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_me'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Me',
        ),
    ]
