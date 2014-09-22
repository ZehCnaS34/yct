# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0007_auto_20140921_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'active company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'active employee'),
        ),
    ]
