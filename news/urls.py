import os

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^get_news/$',
      views.get_news_for_location),
]