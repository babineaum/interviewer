# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recruiter_name', models.CharField(max_length=255)),
                ('recruiter_company', models.CharField(max_length=255)),
                ('recruiter_email', models.EmailField(max_length=254)),
                ('recruiter_companies', models.CharField(max_length=255)),
                ('recruiter_notes', models.TextField()),
                ('recruiter_contact_date', models.DateField(auto_now_add=True)),
                ('recruiter_contact_date_latest', models.DateField(auto_now=True)),
                ('recruiter_follow_up', models.CommaSeparatedIntegerField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
