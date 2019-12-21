""" apps/billets/views.py """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Billet


class AgendaView(LoginRequiredMixin, ListView):
    """ Agenda (main page of the app). """
    template_name = "billets/agenda.html"
    queryset = Billet.objects.all()


def create(request):
    """ Create billet. """
    return render(request, 'billets/form.html')


def detail(request):
    """ Detail of billet. """
    return render(request, 'billets/detail.html')


def update(request):
    """ Update billet. """
    return render(request, 'billets/form.html')
