# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_consumer_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(default=b'Anonymous', max_length=128),
            preserve_default=True,
        ),
    ]
