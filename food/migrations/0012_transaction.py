# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_auto_20150124_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.IntegerField(default=0)),
                ('drop_off', models.CharField(default=b' ', max_length=128)),
                ('date', models.DateTimeField()),
                ('consumer', models.ForeignKey(to='food.Consumer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
