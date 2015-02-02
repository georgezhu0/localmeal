# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_auto_20150124_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swarthmore_service',
            name='int',
        ),
        migrations.AddField(
            model_name='swarthmore_service',
            name='time',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
