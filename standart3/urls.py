from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.standart_room3, name='standart_room3'),

]
