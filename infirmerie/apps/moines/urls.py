""" apps/moines/urls.py """

from django.urls import path

from . import views

app_name = 'moines'
urlpatterns = [
    path('', views.MoineListView.as_view(), name='list'),
    path('create', views.MoineCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.moine_detail_view, name='detail'),
    path('id=<int:pk>/update', views.MoineUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.MoineDeleteView.as_view(), name='delete'),
]
