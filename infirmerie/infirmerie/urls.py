""" Routeur of Infirmerie. """

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('billets/', include('apps.billets.urls')),
    path('moines/', include('apps.moines.urls')),
    path('toubibs/', include('apps.toubibs.urls')),
]
