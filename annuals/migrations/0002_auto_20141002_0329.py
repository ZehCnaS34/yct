# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annuals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualresponse',
            name='annual_meeting',
        ),
        migrations.RemoveField(
            model_name='annualresponse',
            name='employee',
        ),
        migrations.DeleteModel(
            name='AnnualResponse',
        ),
    ]
