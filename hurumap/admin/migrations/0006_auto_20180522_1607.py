# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-22 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_blogpage_featured_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='BlogPostPage',
        ),
    ]