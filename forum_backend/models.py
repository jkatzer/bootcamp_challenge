from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField


class ForumBaseModel(TimeStampedModel):
	username = models.CharField( _( 'username'), max_length=80 )
	# django-extensions calls their vars created, modified. The specs asked for created_at and modified_at, so implemented as getters.
	def created_at(self):
		return "%d-%d-%d %d:%d" % (self.created.day, self.created.month, self.created.year, self.created.hour, self.created.minute)

	def modified_at(self):
		return "%d-%d-%d %d:%d" % (self.modified.day, self.modified.month, self.modified.year, self.modified.hour, self.modified.minute)

	class Meta:
		abstract = True


class Thread(ForumBaseModel):
    """
    The Thread. Comments are associated through their own ForeignKey
    """
    # base fields as described in the functional requirement doc
    title = models.CharField( _('title'), max_length=255)
    description = models.TextField( _('description'), blank=True )
    # for nice url views and specifics
    slug = AutoSlugField( _('slug'), populate_from='title', primary_key=True )
    # maybe implement functionality for admins? 
    thread_open = models.BooleanField( _('open'), default=True)
    # other things for quicker viewing. They're nice to have! Comment in string because we haven't defined yet. Django helper
    last_comment = models.ForeignKey('Comment', related_name='last_comment', blank=True, default=None, null=True)
    num_replies = models.IntegerField(default=0)


    def get_comments(self):
    	return Comment.objects.filter(thread=self)
    
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
	thread = models.ForeignKey( Thread, related_name='comments' )

	def __str__(self):
		time = "%d-%d-%d" % (self.created.day, self.created.month, self.created.year)
		return "%s %s | score: %d" % (self.username, time, self.score) 

	class Meta:
		# Make initial ordering descending based on score. 
		# NOTE: Possibly use order_with_respect_to but don't see what that changes over setting score.
		ordering = ['-score']
