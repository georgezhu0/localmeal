# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_consumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='addressline1',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumer',
            name='city',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumer',
            name='name',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
    ]
