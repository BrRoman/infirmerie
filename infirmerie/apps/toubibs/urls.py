""" apps/toubibs/urls.py """

from django.urls import path

from .views import ToubibCreateView, ToubibDeleteView, \
    ToubibDetailView, ToubibListView, ToubibUpdateView

app_name = 'toubibs'
urlpatterns = [
    path('page=<int:page>', ToubibListView.as_view(), name='list'),
    path('create', ToubibCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', ToubibDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', ToubibUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', ToubibDeleteView.as_view(), name='delete'),
]
