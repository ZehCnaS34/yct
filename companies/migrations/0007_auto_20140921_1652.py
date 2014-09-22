# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20140921_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='active',
            field=models.BooleanField(verbose_name='active company', default=True),
        ),
    ]
