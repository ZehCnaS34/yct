# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40, choices=[(b'nj', b'New Jersey'), (b'wa', b'Washington'), (b'ny', b'New York')])),
                ('contry', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True, verbose_name=b'active company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('street', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40, null=True)),
                ('state', models.CharField(max_length=40, choices=[(b'nj', b'New Jersey'), (b'wa', b'Washington'), (b'ny', b'New York')])),
                ('country', models.CharField(max_length=40, null=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'active employee')),
                ('company', models.ForeignKey(to='companies.Company', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
