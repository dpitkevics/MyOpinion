# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20150430_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
