""" apps/moines/views.py """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from apps.billets.models import Billet
from .forms import MoineForm
from .models import Moine


class MoineListView(LoginRequiredMixin, ListView):
    """ List of Moines. """
    template_name = 'moines/list.html'
    paginate_by = 1000
    queryset = Moine.objects.order_by('nom_religieux', 'prenom_civil')


class MoineCreateView(LoginRequiredMixin, CreateView):
    """ Create Moine. """
    model = Moine
    form_class = MoineForm
    template_name = 'moines/form.html'
    success_url = reverse_lazy('moines:list')


def moine_detail_view(request, **kwargs):
    """ Detail of Moine. """
    moine = Moine.objects.get(id=kwargs['pk'])
    rendez_vous_1 = Billet.objects.filter(moine1=moine)
    rendez_vous_2 = Billet.objects.filter(moine2=moine)
    rendez_vous = rendez_vous_1.union(rendez_vous_2)
    return render(
        request,
        'moines/detail.html',
        {
            'moine': moine,
            'rendez_vous': rendez_vous,
        }
    )


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
