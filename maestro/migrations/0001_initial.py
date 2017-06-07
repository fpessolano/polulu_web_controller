# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('rangeMin', models.IntegerField(default=0)),
                ('rangeMax', models.IntegerField(default=0)),
                ('target', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('acceleration', models.IntegerField(default=0)),
            ],
        ),
    ]
