# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_college_meals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swarthmore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meals', models.IntegerField(default=0)),
                ('menu', models.CharField(default=b' ', max_length=128)),
                ('int', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='college',
            name='user',
        ),
        migrations.DeleteModel(
            name='College',
        ),
    ]
