# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('e_type', models.CharField(default=b'ta', max_length=2, choices=[(b'pa', b'Paragraph'), (b'rd', b'Radio'), (b'cb', b'CheckBox'), (b'tx', b'text'), (b'ta', b'textarea')])),
                ('value', models.CharField(default=b'element filler', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('fields', models.ManyToManyField(to='forms.Element')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
