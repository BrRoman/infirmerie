""" apps/moines/views.py """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import MoineForm
from .models import Moine


class MoineListView(LoginRequiredMixin, ListView):
    """ List of Moines. """
    template_name = 'moines/list.html'
    paginate_by = 1000
    queryset = Moine.objects.order_by(
        'date_naissance', 'nom_religieux', 'prenom_civil')


class MoineCreateView(LoginRequiredMixin, CreateView):
    """ Create Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list')


class MoineDetailView(LoginRequiredMixin, DetailView):
    """ Detail of Moine. """
    fields = ('__all__')
    model = Moine
    template_name = 'moines/detail.html'


class MoineUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list')


class MoineDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete moine. """
    model = Moine
    success_url = reverse_lazy('moines:list')
    template_name = "moines/delete.html"
