# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annuals', '0006_auto_20140927_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualmeeting',
            name='notified_date',
            field=models.DateTimeField(null=True, verbose_name=b'notified date'),
        ),
        migrations.AlterField(
            model_name='annualmeeting',
            name='response_date',
            field=models.DateTimeField(null=True, verbose_name=b'reponse date'),
        ),
    ]
