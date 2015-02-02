# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_transaction_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='zipcode',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
