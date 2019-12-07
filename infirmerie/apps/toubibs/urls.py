from django.urls import path

from . import views

app_name = 'toubibs'
urlpatterns = [
    path('list', views.list, name='list'),
]
