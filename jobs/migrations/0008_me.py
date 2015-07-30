# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20150729_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=20)),
                ('twitter', models.CharField(max_length=20)),
                ('facebook', models.CharField(max_length=20)),
                ('instagram', models.CharField(max_length=20)),
                ('linkedin', models.CharField(max_length=20)),
            ],
        ),
    ]
