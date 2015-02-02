# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0019_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='zipcode',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
