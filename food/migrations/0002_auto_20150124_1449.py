# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='category',
        ),
        migrations.DeleteModel(
            name='Consumer',
        ),
    ]
