# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='notes',
            field=models.TextField(),
        ),
    ]
