from django.db import models
from django.utils.translation import gettext as _

from tools.basemodel.models import TimestampedModel


class ForumBaseModel(TimestampedModel):
	username = models.CharField(_( 'username'), max_length=80 )

	class Meta:
		abstract = True


class Thread(ForumBaseModel):
    """
    The Thread. Comments are associated through their own ForeignKey
    """
    # base fields as described in the functional requirement doc
    title = models.CharField( _('title'), max_length=255)
    description = models.TextField( 'description', blank=True )
    # for nice url views and specifics
    slug = models.SlugField( _('slug') )
    # maybe implement functionality for admins?
    thread_open = models.BooleanField(default=True)
    
    # proper thread display
    def __str__(self):
		return self.title
	# just in case, with Python 2.x
    def __unicode__(self):
		return self.title


class Comment(ForumBaseModel):
	"""
	The Comment. Ordered by highest score and each related to a single thread.
	""" 
	content = models.TextField( _('content') )
	score = models.IntegerField( _('score'), default=0 )
	thread = models.ForeignKey( _('thread'), Thread )

	class Meta:
		# Make initial ordering descending based on score. 
		# NOTE: Possibly use order_with_respect_to but don't see what that changes over setting score.
		ordering = ['-score']










# Create your models here.
