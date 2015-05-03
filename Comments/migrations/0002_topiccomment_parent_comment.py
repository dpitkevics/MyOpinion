# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topiccomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, to='Comments.TopicComment'),
        ),
    ]
