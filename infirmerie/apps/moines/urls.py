from django.urls import path

from . import views

app_name = 'moines'
urlpatterns = [
    path('', views.list, name='list'),
    path('create', views.create, name='create'),
    path('detail', views.detail, name='detail'),
    path('update', views.update, name='update')
]
