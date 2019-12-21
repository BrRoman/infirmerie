""" Routeur of Infirmerie. """

from django.contrib import admin
from django.urls import include, path

from apps.billets import views as billets_views

urlpatterns = [
    path('', billets_views.AgendaView.as_view(), name='agenda'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('billets/', include('apps.billets.urls')),
    path('moines/', include('apps.moines.urls')),
    path('toubibs/', include('apps.toubibs.urls')),
]
