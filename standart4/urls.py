from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.standart_room4, name='standart_room4'),
]
