""" Routeur of Infirmerie. """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('infirmerie/', include('apps.main.urls')),
    path('infirmerie/admin/', admin.site.urls),
    path('infirmerie/accounts/', include('apps.accounts.urls')),
    path('infirmerie/billets/', include('apps.billets.urls')),
    path('infirmerie/moines/', include('apps.moines.urls')),
    path('infirmerie/toubibs/', include('apps.toubibs.urls')),
]
