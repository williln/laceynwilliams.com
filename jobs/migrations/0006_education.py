# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20150729_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('university', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('grad_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('degree', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
    ]
