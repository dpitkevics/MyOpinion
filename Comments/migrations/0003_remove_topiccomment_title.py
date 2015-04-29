# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0002_topiccomment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topiccomment',
            name='title',
        ),
    ]
