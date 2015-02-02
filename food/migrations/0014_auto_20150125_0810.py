# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20150125_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='haverford_service',
            name='bar1',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='haverford_service',
            name='bar2',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='swarthmore_service',
            name='homestyle',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='swarthmore_service',
            name='specialty',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='swarthmore_service',
            name='vegetarian',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
    ]
