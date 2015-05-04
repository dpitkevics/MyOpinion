# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0002_topiccomment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccomment',
            name='parent_comment',
            field=models.ForeignKey(to='Comments.TopicComment', related_name='children_comment_set', null=True, blank=True),
        ),
    ]
