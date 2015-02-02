# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20150124_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='meals',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
