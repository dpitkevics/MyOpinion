# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Topics', '0002_auto_20150428_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='latest_action_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 10, 16, 38, 574151, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topictag',
            name='topics',
            field=models.ManyToManyField(to='Topics.Topic', blank=True),
        ),
    ]
