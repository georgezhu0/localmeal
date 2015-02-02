# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_auto_20150125_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
    ]
