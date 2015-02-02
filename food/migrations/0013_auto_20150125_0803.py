# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haverford_service',
            name='time',
        ),
        migrations.RemoveField(
            model_name='swarthmore_service',
            name='time',
        ),
    ]
