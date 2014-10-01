# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20140930_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'active employee'),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
