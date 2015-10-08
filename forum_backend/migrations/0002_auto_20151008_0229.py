# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='last_comment',
            field=models.ForeignKey(related_name='last_comment', blank=True, to='forum_backend.Comment'),
        ),
    ]
