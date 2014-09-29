# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annuals', '0005_auto_20140927_1944'),
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
        migrations.AddField(
            model_name='annualmeeting',
            name='notified_date',
            field=models.DateTimeField(default=0, verbose_name=b'notified date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annualmeeting',
            name='response_date',
            field=models.DateTimeField(default=0, verbose_name=b'reponse date'),
            preserve_default=False,
        ),
    ]
