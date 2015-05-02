# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('user_name', models.CharField(blank=True, max_length=50, verbose_name="user's name")),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name="user's email address")),
                ('user_url', models.URLField(blank=True, verbose_name="user's URL")),
                ('comment', models.TextField(max_length=3000, verbose_name='comment')),
                ('submit_date', models.DateTimeField(default=None, verbose_name='date/time submitted')),
                ('ip_address', models.GenericIPAddressField(blank=True, unpack_ipv4=True, verbose_name='IP address', null=True)),
                ('is_public', models.BooleanField(help_text='Uncheck this box to make the comment effectively disappear from the site.', default=True, verbose_name='is public')),
                ('is_removed', models.BooleanField(help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', default=False, verbose_name='is removed')),
                ('content_type', models.ForeignKey(related_name='content_type_set_for_topiccomment', to='contenttypes.ContentType', verbose_name='content type')),
                ('site', models.ForeignKey(to='sites.Site')),
                ('user', models.ForeignKey(related_name='topiccomment_comments', to=settings.AUTH_USER_MODEL, blank=True, verbose_name='user', null=True)),
            ],
            options={
                'permissions': [('can_moderate', 'Can moderate comments')],
                'verbose_name': 'comment',
                'ordering': ('-submit_date',),
                'verbose_name_plural': 'comments',
            },
        ),
    ]
