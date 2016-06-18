# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shudata', '0005_auto_20160618_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='Service_Areas',
            field=djgeojson.fields.PolygonField(default={}),
        ),
    ]
