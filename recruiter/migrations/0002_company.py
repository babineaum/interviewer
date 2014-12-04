# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=255)),
                ('hiring_manager', models.CharField(max_length=255)),
                ('hiring_mngr_email', models.EmailField(max_length=254)),
                ('company_notes', models.TextField()),
                ('company_contact_date', models.DateField(auto_now_add=True)),
                ('company_contact_date_latest', models.DateField(auto_now=True)),
                ('company_follow_up', models.CommaSeparatedIntegerField(max_length=512)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
