from django.conf.urls import url

from . import views

urlpattterns = [
    url(r'^$', views.index, name='index'),
]