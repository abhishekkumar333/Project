# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Service_Areas', djgeojson.fields.PolygonField()),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('email', models.CharField(default=b'', max_length=30, blank=True)),
                ('phone', models.CharField(default=b'', max_length=15, blank=True)),
                ('Language', models.CharField(default=b'', max_length=20, blank=True)),
                ('Currency', models.CharField(default=b'', max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
