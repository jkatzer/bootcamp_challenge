from django.db import models
from django_extensions.db.models import TimeStampedModel

from .fields import CreationDateTimeField, ModificationDateTimeField


class TimestampedSlugModel(TimeStampedModel):
    """ 
    BaseModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.

    Formally known as TimeStampedModel by Django-Extensions:
    https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/models.py
    """
    created_at = CreationDateTimeField( _('created') )
    modified_at = ModificationDateTimeField( _('modified') )

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True