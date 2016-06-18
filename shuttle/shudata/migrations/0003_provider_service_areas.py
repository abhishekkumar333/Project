# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shudata', '0002_remove_provider_service_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='Service_Areas',
            field=djgeojson.fields.PolygonField(default=[]),
            preserve_default=True,
        ),
    ]
