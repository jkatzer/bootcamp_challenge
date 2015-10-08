from rest_framework import serializers

from .models import Thread, Comment


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Thread


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment

	def create(data):
		instance = super(CommentSerializer, self).create(**data)
		instance.thread.last_comment = instance
		instance.thread.num_replies += 1
		instance.thread.save()
		return instance