""" apps/billets/urls.py """

from django.urls import path, re_path

from . import views

app_name = 'billets'
urlpatterns = [
    re_path(r'^agenda/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$',
            views.AgendaView.as_view(), name='agenda'),
    path('create', views.BilletCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.BilletDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.BilletUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.BilletDeleteView.as_view(), name='delete'),
    path('id=<int:pk>/pdf', views.BilletPDFView.as_view(), name='pdf'),
]
