from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response


from .models import Thread, Comment
from .serializers import ThreadSerializer, CommentSerializer


# Create your views here.

def indexView(request):
	return render(request, 'base.html')

class ThreadViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint that allows threads to be viewed or edited
	"""
	queryset = Thread.objects.all().order_by('-modified')
	serializer_class = ThreadSerializer

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def comments(self, request, *args, **kwargs):
		comments = self.results[0].get_comments()
		return Response(comments)

class CommentViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint that allows comments to be viewed, edited, created
	"""
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer