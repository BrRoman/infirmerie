""" apps/moines/urls.py """

from django.urls import path

from .views import MoineCreateView, MoineDeleteView, MoineDetailView, MoineListView, MoineUpdateView

app_name = 'moines'
urlpatterns = [
    path('page=<int:page>', MoineListView.as_view(), name='list'),
    path('create', MoineCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', MoineDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', MoineUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', MoineDeleteView.as_view(), name='delete'),
]
