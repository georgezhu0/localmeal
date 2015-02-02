# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20150124_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haverford',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meals', models.IntegerField(default=0)),
                ('menu', models.CharField(default=b' ', max_length=128)),
                ('time', models.TimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
