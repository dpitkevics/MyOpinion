# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('user_name', models.CharField(verbose_name="user's name", max_length=50, blank=True)),
                ('user_email', models.EmailField(verbose_name="user's email address", max_length=254, blank=True)),
                ('user_url', models.URLField(verbose_name="user's URL", blank=True)),
                ('comment', models.TextField(verbose_name='comment', max_length=3000)),
                ('submit_date', models.DateTimeField(verbose_name='date/time submitted', default=None)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP address', unpack_ipv4=True, blank=True)),
                ('is_public', models.BooleanField(verbose_name='is public', help_text='Uncheck this box to make the comment effectively disappear from the site.', default=True)),
                ('is_removed', models.BooleanField(verbose_name='is removed', help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', default=False)),
                ('content_type', models.ForeignKey(related_name='content_type_set_for_topiccomment', to='contenttypes.ContentType', verbose_name='content type')),
                ('site', models.ForeignKey(to='sites.Site')),
                ('user', models.ForeignKey(related_name='topiccomment_comments', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='user')),
            ],
            options={
                'verbose_name': 'comment',
                'permissions': [('can_moderate', 'Can moderate comments')],
                'verbose_name_plural': 'comments',
                'ordering': ('-submit_date',),
            },
        ),
    ]
