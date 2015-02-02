# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0025_auto_20150125_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='school',
            field=models.CharField(max_length=10, choices=[(b'Swarthmore', b'Swarthmore'), (b'Haverford', b'Haverford')]),
            preserve_default=True,
        ),
    ]
