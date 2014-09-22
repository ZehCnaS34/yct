# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20140921_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=40, choices=[('nj', 'New Jersey'), ('wa', 'Washington'), ('ny', 'New York')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(max_length=40, choices=[('nj', 'New Jersey'), ('wa', 'Washington'), ('ny', 'New York')]),
        ),
    ]
