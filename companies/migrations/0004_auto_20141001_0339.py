# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20141001_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'active'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'active'),
        ),
    ]
