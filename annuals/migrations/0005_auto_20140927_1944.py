# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20140923_1631'),
        ('annuals', '0004_continueeducationresponse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response_date', models.DateTimeField(verbose_name=b'reponse date')),
                ('notified_date', models.DateTimeField(verbose_name=b'notified date')),
                ('annual_meeting', models.ForeignKey(to='annuals.AnnualMeeting')),
                ('employee', models.ForeignKey(to='companies.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='annualmeetingresponse',
            name='annual_meeting',
        ),
        migrations.RemoveField(
            model_name='annualmeetingresponse',
            name='employee',
        ),
        migrations.DeleteModel(
            name='AnnualMeetingResponse',
        ),
        migrations.RemoveField(
            model_name='continueeducation',
            name='company',
        ),
        migrations.RemoveField(
            model_name='continueeducation',
            name='reference_links',
        ),
        migrations.RemoveField(
            model_name='continueeducationresponse',
            name='continue_education',
        ),
        migrations.DeleteModel(
            name='ContinueEducation',
        ),
        migrations.RemoveField(
            model_name='continueeducationresponse',
            name='employee',
        ),
        migrations.DeleteModel(
            name='ContinueEducationResponse',
        ),
        migrations.AddField(
            model_name='annualmeeting',
            name='annual_type',
            field=models.CharField(default=b'am', max_length=2, choices=[(b'am', b'Annual Meeting'), (b'ce', b'Continue Education')]),
            preserve_default=True,
        ),
    ]
