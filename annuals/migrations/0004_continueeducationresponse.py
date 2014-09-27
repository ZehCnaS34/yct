# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20140923_1631'),
        ('annuals', '0003_annualmeetingresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinueEducationResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response_date', models.DateTimeField(verbose_name=b'reponse date')),
                ('continue_education', models.ForeignKey(to='annuals.ContinueEducation')),
                ('employee', models.ForeignKey(to='companies.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
