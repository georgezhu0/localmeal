# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_haverford'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Haverford',
            new_name='Haverford_Service',
        ),
        migrations.RenameModel(
            old_name='Swarthmore',
            new_name='Swarthmore_Service',
        ),
    ]
