from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('main.urls')),
    url(r'^contact', include('contact.urls')),
    url(r'^rooms', include('rooms.urls')),
    url(r'^standart1', include('standart1.urls')),
    url(r'^standart2', include('standart2.urls')),
    url(r'^family_room', include('family_room.urls')),
    url(r'^information', include('information.urls')),
    url(r'^example', include('example.urls')),
    url(r'^standart3', include('standart3.urls')),
    url(r'^standart4', include('standart4.urls')),
    url(r'^standart5', include('standart5.urls')),
    url(r'^standart7', include('standart7.urls')),
    url(r'^standart8', include('standart8.urls')),
    url(r'^standart9', include('standart9.urls')),
    url(r'^standart10', include('standart10.urls')),
    url(r'^standart11', include('standart11.urls')),
    url(r'^standart12', include('standart12.urls')),







]
