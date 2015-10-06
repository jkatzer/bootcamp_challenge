from django.db import models
from django.utils.translation import gettext as _

from .fields import CreationDateTimeField, ModificationDateTimeField


class TimestampedModel(models.Model):
    """ 
    BaseModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.

    Formally known as TimeStampedModel by Django-Extensions:
    https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/models.py
    """
    created = CreationDateTimeField( _('created') )
    modified = ModificationDateTimeField( _('modified') )

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True