# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('username', models.CharField(max_length=80, verbose_name='username')),
                ('content', models.TextField(verbose_name='content')),
                ('score', models.IntegerField(default=0, verbose_name='score')),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('username', models.CharField(max_length=80, verbose_name='username')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'title', verbose_name='slug', editable=False, blank=True)),
                ('thread_open', models.BooleanField(default=True, verbose_name='open')),
                ('num_replies', models.IntegerField(default=0)),
                ('last_comment', models.ForeignKey(related_name='last_comment', to='forum_backend.Comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(to='forum_backend.Thread'),
        ),
    ]
