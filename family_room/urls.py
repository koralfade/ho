from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.family_room, name='family_room'),
]
