# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_auto_20150429_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, to='django_comments.Comment', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_comments.comment',),
        ),
    ]
