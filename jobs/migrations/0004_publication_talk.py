# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publications', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('conference', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('talk_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField()),
            ],
        ),
    ]
