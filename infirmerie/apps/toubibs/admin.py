""" apps/toubibs/admin.py """

from django.contrib import admin
from .models import Specialities, Toubib

admin.site.register(Specialities)
admin.site.register(Toubib)
