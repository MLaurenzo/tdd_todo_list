from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^todos/$', views.todo_list),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.todo_detail),
]