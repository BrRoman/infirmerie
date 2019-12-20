""" apps/moines/views.py """

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Moine
from .forms import MoineForm


class MoineListView(ListView):  # pylint: disable=too-many-ancestors
    """ List of Moines. """
    template_name = 'moines/list.html'
    paginate_by = 5
    queryset = Moine.objects.order_by(
        'date_naissance', 'nom_religieux', 'prenom_civil')


class MoineCreateView(CreateView):
    """ Create Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list', args=[1])


class MoineDetailView(DetailView):
    """ Detail of Moine. """
    fields = ('__all__')
    model = Moine
    template_name = 'moines/detail.html'


class MoineUpdateView(UpdateView):
    """ Update Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list', args=[1])


class MoineDeleteView(DeleteView):
    """ Delete moine. """
    model = Moine
    success_url = reverse_lazy('moines:list', args=[1])
    template_name = "moines/delete.html"
