""" apps/toubibs/views.py """

from dal import autocomplete

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ToubibForm
from .models import Speciality, Toubib


class ToubibListView(LoginRequiredMixin, ListView):
    """ List of Toubibs. """
    template_name = 'toubibs/list.html'
    paginate_by = 20

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


class ToubibAutocompleteView(autocomplete.Select2QuerySetView):
    """ Return a set of Toubibs according to the user search value. """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Toubib.objects.none()

        toubibs = Toubib.objects.all()
        if self.q:
            toubibs = toubibs.filter(nom__istartswith=self.q)
        return toubibs


@login_required
def specialities_list(request):
    """ List of specialities. """
    specialities = Speciality.objects.all().order_by('speciality')
    return render(
        request,
        'specialities/list.html',
        {
            'specialities': specialities
        }
    )


@login_required
def specialities_create(request):
    """ Create a speciality. """
    pass


@login_required
def specialities_update(request):
    """ Update a speciality. """
    pass


@login_required
def specialities_delete(request):
    """ Delete a speciality. """
    pass
