# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-16 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurumap', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataIndicatorAuthor',
            new_name='DataIndicatorPublisher',
        ),
        migrations.RenameField(
            model_name='dataindicator',
            old_name='author',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='dataindicator',
            old_name='author_code',
            new_name='publisher_code',
        ),
        migrations.RenameField(
            model_name='dataindicator',
            old_name='author_data',
            new_name='publisher_data',
        ),
        migrations.RenameField(
            model_name='dataindicatorvalue',
            old_name='author_data',
            new_name='publisher_data',
        ),
    ]
