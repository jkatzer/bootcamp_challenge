from django.views.decorators.csrf import csrf_exempt

from rest_framework import serializers

from .models import Thread, Comment



class CommentSerializer(serializers.HyperlinkedModelSerializer):
	#thread = serializers.StringRelatedField(read_only=True, source='thread.slug')
	class Meta:
		model = Comment

	def create(self, data):
		instance = Comment.objects.create(**data)
		instance.thread.last_comment = instance
		instance.thread.num_replies += 1
		instance.thread.save()
		return instance

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
	slug = serializers.CharField(read_only=True)
	comments = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Thread