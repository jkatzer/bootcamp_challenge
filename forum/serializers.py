from rest_framework import serializers

from .models import Thread, Comment


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Thread


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment