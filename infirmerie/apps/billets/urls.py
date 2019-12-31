""" apps/billets/urls.py """

from django.urls import path

from . import views

app_name = 'billets'
urlpatterns = [
    path('', views.AgendaView.as_view(), name='agenda'),
    path('create', views.create, name='create'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('update', views.update, name='update')
]
