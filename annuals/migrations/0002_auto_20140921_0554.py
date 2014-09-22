# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('annuals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualmeeting',
            name='company',
            field=models.ForeignKey(default=0, to='companies.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='continueeducation',
            name='company',
            field=models.ForeignKey(default=0, to='companies.Company'),
            preserve_default=False,
        ),
    ]
