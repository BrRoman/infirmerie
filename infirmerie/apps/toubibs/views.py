""" apps/toubibs/views.py """

from dal import autocomplete

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import SpecialityForm, ToubibForm
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


@login_required
def toubibs_repertoire(request, **kwargs):
    """ Toubibs as repertoire. """
    toubibs = Toubib.objects.filter(
        nom__startswith=kwargs['letter']).order_by('nom', 'prenom')
    return render(
        request,
        'toubibs/repertoire.html',
        {
            'letters': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-'],
            'toubibs': toubibs,
            'current': kwargs['letter'],
        }
    )


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
    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm()

    return render(
        request,
        'specialities/form.html',
        {'form': form}
    )


@login_required
def specialities_update(request, **kwargs):
    """ Update a speciality. """
    spe = get_object_or_404(Speciality, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=spe)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm(instance=spe)

    return render(
        request,
        'specialities/form.html',
        {
            'form': form,
            'spe': spe,
        }
    )


@login_required
def specialities_delete(request, **kwargs):
    """ Delete a speciality. """
    spe = get_object_or_404(Speciality, pk=kwargs['pk'])

    if request.method == 'POST':
        form = SpecialityForm(request.POST)
        spe.delete()
        return HttpResponseRedirect(reverse('toubibs:specialities_list'))

    else:
        form = SpecialityForm()

    return render(request, 'specialities/delete.html', {
        'form': form,
        'spe': spe,
    })
