# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualMeeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('annual_type', models.CharField(default=b'am', max_length=2, choices=[(b'am', b'Annual Meeting'), (b'ce', b'Continue Education')])),
                ('year', models.DateTimeField(verbose_name=b'annual year')),
                ('response_date', models.DateTimeField(null=True, verbose_name=b'response date')),
                ('notified_date', models.DateTimeField(null=True, verbose_name=b'notified date')),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnnualResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annual_meeting', models.ForeignKey(to='annuals.AnnualMeeting')),
                ('employee', models.ForeignKey(to='companies.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=250)),
                ('display', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='annualmeeting',
            name='reference_links',
            field=models.ManyToManyField(to='annuals.ReferenceLink'),
            preserve_default=True,
        ),
    ]
