""" apps/billets/urls.py """

from django.urls import path, re_path

from apps.billets import views

app_name = 'billets'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'^agenda/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$',
            views.AgendaView.as_view(), name='agenda'),
    path('list', views.billets_list_view, name='list'),
    path('list/page=<int:page>', views.billets_list_view, name='list_page'),
    path('create', views.BilletCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.BilletDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.BilletUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.BilletDeleteView.as_view(), name='delete'),
    path('id=<int:pk>/pdf', views.BilletPDFView.as_view(), name='pdf'),
]
