""" Routeur of Infirmerie. """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('billets/', include('apps.billets.urls')),
    path('moines/', include('apps.moines.urls')),
    path('toubibs/', include('apps.toubibs.urls')),
]
