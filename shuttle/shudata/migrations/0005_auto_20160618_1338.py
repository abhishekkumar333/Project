# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shudata', '0004_auto_20160618_1330'),
    ]

    operations = [
        migrations.DeleteModel(
            name='poly',
        ),
        migrations.AddField(
            model_name='provider',
            name='Service_Areas',
            field=djgeojson.fields.PointField(default={}),
            preserve_default=True,
        ),
    ]
