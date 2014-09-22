# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(choices=[('nj', 'New Jersey'), ('va', 'Atl'), ('ny', 'New York')], max_length=40),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('nj', 'New Jersey'), ('va', 'Atl'), ('ny', 'New York')], max_length=40),
        ),
    ]
