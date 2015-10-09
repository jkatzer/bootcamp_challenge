from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

import views as forum_views


# set up REST API framework router
router = routers.DefaultRouter()
router.register(r'threads', forum_views.ThreadViewSet)
router.register(r'comments', forum_views.CommentViewSet)



urlpatterns = [
    # Examples:
    # url(r'^$', 'bootcamp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls) ),
    url(r'^', forum_views.indexView),
]
