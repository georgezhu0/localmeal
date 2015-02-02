# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0024_transaction_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='school',
            field=models.CharField(default=b' ', max_length=128),
            preserve_default=True,
        ),
    ]
