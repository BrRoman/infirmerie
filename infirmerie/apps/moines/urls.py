""" apps/moines/urls.py """

from django.urls import path

from .views import MoineCreateView, MoineDetailView, MoineListView, MoineUpdateView

app_name = 'moines'
urlpatterns = [
    path('', MoineListView.as_view(), name='list'),
    path('create', MoineCreateView.as_view(), name='create'),
    path('<int:pk>/detail', MoineDetailView.as_view(), name='detail'),
    path('<int:pk>/update', MoineUpdateView.as_view(), name='update'),
]
