from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^get_news/$',
        views.get_news_for_location),
    path('list/', views.render_news, name='locationNews')

]
