from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.standart_room9, name='standart_room9'),
]
