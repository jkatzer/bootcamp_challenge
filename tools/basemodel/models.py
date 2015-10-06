from django.db import models


class BaseModel(models.Model):
    """ 
    BaseModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields as well as title and slug.

    Formally known as TimeStampedModel by Django-Extensions:
    https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/models.py
    """
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug', max_length=255))

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True