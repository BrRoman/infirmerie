""" apps/toubibs/admin.py """

from django.contrib import admin
from .models import Speciality, Toubib

admin.site.register(Speciality)
admin.site.register(Toubib)
