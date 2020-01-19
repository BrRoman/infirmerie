""" apps/billets/views.py """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from reportlab.pdfgen import canvas

from .forms import BilletForm
from .models import Billet


class AgendaView(LoginRequiredMixin, ListView):
    """ Agenda (main page of the app). """
    template_name = "billets/agenda.html"
    paginate_by = 5
    queryset = Billet.objects.all().order_by('-when')


class BilletCreateView(LoginRequiredMixin, CreateView):
    """ Create Billet. """
    model = Billet
    form_class = BilletForm
    template_name = 'billets/form.html'
    success_url = reverse_lazy('billets:agenda', args=[1])


class BilletDetailView(LoginRequiredMixin, DetailView):
    """ Detail of Billet. """
    fields = ('__all__')
    model = Billet
    template_name = 'billets/detail.html'


class BilletUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Billet. """
    model = Billet
    form_class = BilletForm
    template_name = 'billets/form.html'
    success_url = reverse_lazy('billets:agenda', args=[1])


class BilletDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete billet. """
    model = Billet
    success_url = reverse_lazy('billets:agenda', args=[1])
    template_name = "billets/delete.html"


class BilletPDFView(View):
    """ Display billet as pdf. """

    def get(self):
        """ Get pdf. """
        pdf = canvas.Canvas("apps/billets/hello.pdf")
        pdf.drawString(100, 100, "Hello World")
        pdf.showPage()
        pdf.save()
        return HttpResponse('Hello pdf!')
