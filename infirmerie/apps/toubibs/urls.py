""" apps/toubibs/urls.py """

from django.urls import path, re_path

from . import views

app_name = 'toubibs'
urlpatterns = [
    re_path(r'^(search=(?P<search>\w+)/)?page=(?P<page>\d+)/$',
            views.ToubibListView.as_view(), name='list'),
    path('create', views.ToubibCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.ToubibDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.ToubibUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.ToubibDeleteView.as_view(), name='delete'),
]
