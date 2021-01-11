""" apps/toubibs/urls.py """

from django.urls import path, re_path

from . import views

app_name = 'toubibs'
urlpatterns = [
    # Toubibs:
    re_path(r'^(search=(?P<search>\w+)/)?page=(?P<page>\d+)$',
            views.ToubibListView.as_view(), name='list'),
    path('repertoire/<letter>', views.toubibs_repertoire, name='repertoire'),
    path('create', views.ToubibCreateView.as_view(), name='create'),
    path('id=<int:pk>/detail', views.ToubibDetailView.as_view(), name='detail'),
    path('id=<int:pk>/update', views.ToubibUpdateView.as_view(), name='update'),
    path('id=<int:pk>/delete', views.ToubibDeleteView.as_view(), name='delete'),
    # Autocomplete:
    path('autocomplete/',
         views.ToubibAutocompleteView.as_view(), name='autocomplete'),
    # Specialities:
    path('specialities/list', views.specialities_list, name='specialities_list'),
    path('specialities/create', views.specialities_create,
         name='specialities_create'),
    path('specialities/<int:pk>/update',
         views.specialities_update, name='specialities_update'),
    path('specialities/<int:pk>/delete',
         views.specialities_delete, name='specialities_delete'),
]
