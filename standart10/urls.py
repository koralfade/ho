from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.standart_room10, name='standart_room10'),
]
