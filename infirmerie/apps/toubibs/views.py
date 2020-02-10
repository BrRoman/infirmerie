""" apps/toubibs/views.py """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ToubibForm
from .models import Toubib


class ToubibListView(LoginRequiredMixin, ListView):
    """ List of Toubibs. """
    template_name = 'toubibs/list.html'
    paginate_by = 50

    def get_queryset(self):
        if 'search' in self.kwargs:
            search = self.kwargs['search']
            queryset = (Toubib.objects.filter(nom__icontains=search)
                        | Toubib.objects.filter(specialite__icontains=search))
        else:
            queryset = Toubib.objects
        return queryset.order_by('nom', 'prenom')


class ToubibCreateView(LoginRequiredMixin, CreateView):
    """ Create Toubib. """
    model = Toubib
    form_class = ToubibForm
    template_name = 'toubibs/form.html'
    success_url = reverse_lazy('toubibs:list', args=[1])


class ToubibDetailView(LoginRequiredMixin, DetailView):
    """ Detail of Toubib. """
    fields = ('__all__')
    model = Toubib
    template_name = 'toubibs/detail.html'


class ToubibUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Toubib. """
    model = Toubib
    form_class = ToubibForm
    template_name = 'toubibs/form.html'
    success_url = reverse_lazy('toubibs:list', args=[1])


class ToubibDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete toubib. """
    model = Toubib
    success_url = reverse_lazy('toubibs:list', args=[1])
    template_name = "toubibs/delete.html"
