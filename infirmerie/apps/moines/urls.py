from django.urls import path

from . import views

app_name = 'moines'
urlpatterns = [
    path('list', views.list, name='list'),
]
