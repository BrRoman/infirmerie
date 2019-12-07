from django.urls import path

from . import views

app_name = 'billets'
urlpatterns = [
    path('list', views.list, name='list'),
]
