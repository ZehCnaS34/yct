# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualMeeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('year', models.DateTimeField(verbose_name='annual year')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContinueEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('year', models.DateTimeField(verbose_name='annual year')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('location', models.CharField(max_length=250)),
                ('display', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='continueeducation',
            name='reference_links',
            field=models.ManyToManyField(to='annuals.ReferenceLink'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annualmeeting',
            name='reference_links',
            field=models.ManyToManyField(to='annuals.ReferenceLink'),
            preserve_default=True,
        ),
    ]
