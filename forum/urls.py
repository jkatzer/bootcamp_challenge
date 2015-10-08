from django.conf.urls import include, url
from django.contrib import admin

import forum.views as forum_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bootcamp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', forum_views.indexView),
]
