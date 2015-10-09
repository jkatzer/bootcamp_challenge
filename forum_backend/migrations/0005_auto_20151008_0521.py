# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_backend', '0004_auto_20151008_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='id',
        ),
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(primary_key=True, populate_from=b'title', serialize=False, editable=False, blank=True, verbose_name='slug'),
        ),
    ]
