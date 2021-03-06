# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=258)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('latest_action_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=258)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Topic Category',
                'ordering': ['title'],
                'verbose_name_plural': 'Topic Categories',
            },
        ),
        migrations.CreateModel(
            name='TopicTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField()),
                ('topics', models.ManyToManyField(blank=True, to='Topics.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(to='Topics.TopicCategory'),
        ),
    ]
