# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invites', '0005_invites_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invites',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]