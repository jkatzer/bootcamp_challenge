from django.shortcuts import render

from rest_framework import viewsets

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

