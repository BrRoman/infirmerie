""" apps/billets/views.py """

import datetime
import io

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from reportlab.lib.pagesizes import A6
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from .forms import BilletForm
from .models import Billet


class HomeView(RedirectView):
    """ Home view: redirect to agenda. """

    def get_redirect_url(self, *args, **kwargs):
        today = datetime.date.today()
        day = today.strftime('%d')
        month = today.strftime('%m')
        year = today.strftime('%Y')
        return reverse('billets:agenda', kwargs={'day': day, 'month': month, 'year': year})


class AgendaView(LoginRequiredMixin, ListView):
    """ Agenda (main page of the app). """
    template_name = "billets/agenda.html"
    queryset = Billet.objects.all().order_by('-when')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date_today = datetime.date.today()
        context['today'] = {'day': date_today.strftime(
            '%d'), 'month': date_today.strftime('%m'), 'year': date_today.strftime('%Y')}

        # Date that has been required in **kwargs:
        display_date = datetime.datetime(
            int(self.kwargs['year']), int(self.kwargs['month']), int(self.kwargs['day']))

        # Initial date of the week containing the required date:
        initial_date = display_date - \
            datetime.timedelta(days=(display_date.weekday() + 1)
                               if display_date.weekday() != 6 else 0)

        # Construct the list of days with all their data:
        days = {}
        for i in range(7):
            date = initial_date + datetime.timedelta(days=i)
            date_human = datetime.date(date.year, date.month, date.day)
            days[date_human] = {}
            days[date_human]['billets'] = Billet.objects.filter(when__gt=date).filter(
                when__lt=(date + datetime.timedelta(days=1)))
            days[date_human]['current'] = (date_human == datetime.date.today())
        context['days'] = days

        return context


class BilletCreateView(LoginRequiredMixin, CreateView):
    """ Create Billet. """
    model = Billet
    form_class = BilletForm
    template_name = 'billets/form.html'
    success_url = reverse_lazy('root')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


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
    success_url = reverse_lazy('root')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class BilletDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete billet. """
    model = Billet
    success_url = reverse_lazy('root')
    template_name = "billets/delete.html"


class BilletPDFView(LoginRequiredMixin, View):
    """ Display billet as pdf. """

    def get(self, request, *args, **kwargs):
        """ Return pdf of billet in browser. """
        billet = Billet.objects.get(pk=self.kwargs['pk'])
        buffer = io.BytesIO()

        # Settings:
        width, height = A6
        pdf = canvas.Canvas(buffer, pagesize=A6, bottomup=0)
        pdf.setFont("Helvetica", 10)
        pdf.saveState()
        pdf.setLineWidth(0.2)

        # Header:
        pdf.drawCentredString(width/2.0, 8 * mm, '+')
        pdf.drawCentredString(width/2.0, 13 * mm, 'PAX')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawCentredString(width/2.0, 55, 'Rendez-vous médical')
        pdf.drawCentredString(width/2.0, 70, billet.date_time())
        pdf.restoreState()
        pdf.saveState()

        # Médecin :
        add = 0
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 33 * mm, 'Médecin')
        pdf.roundRect(7 * mm, 35 * mm, width - 2 * 7 * mm, 30 * mm, 3 * mm)
        pdf.drawString(10 * mm, 40 * mm, billet.toubib.__str__() + (' (Tél. ' +
                                                                    billet.toubib.telephone + ')') if billet.toubib.telephone else '')
        pdf.restoreState()
        if billet.toubib.adresse_1:
            pdf.drawString(15 * mm, 45 * mm, billet.toubib.adresse_1)
        if billet.toubib.adresse_2:
            pdf.drawString(15 * mm, 50 * mm, billet.toubib.adresse_2)
            add += 15
        if billet.toubib.adresse_3:
            pdf.drawString(15 * mm, 55 * mm, billet.toubib.adresse_3)
            add += 15
        if billet.toubib.code_postal and billet.toubib.ville:
            pdf.drawString(15 * mm, 50 * mm + add, billet.toubib.code_postal +
                           ' ' + billet.toubib.ville)
        pdf.saveState()

        # Moine :
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 73 * mm, 'Moine(s) concerné(s)')
        pdf.roundRect(7 * mm, 75 * mm, width - 2 * 7 * mm, 23 * mm, 3 * mm)
        pdf.restoreState()
        pdf.rect(10 * mm, 78 * mm, 2 * mm, 2 * mm)
        pdf.drawString(15 * mm, 80 * mm, billet.moine1.__str__())
        if billet.moine2:
            pdf.rect(10 * mm, 83 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 85 * mm, billet.moine2.__str__())
        if billet.moine3:
            pdf.rect(10 * mm, 88 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 90 * mm, billet.moine3.__str__())
        if billet.moine4:
            pdf.rect(10 * mm, 93 * mm, 2 * mm, 2 * mm)
            pdf.drawString(15 * mm, 95 * mm, billet.moine4.__str__())
        # if billet.moine5:
        #     pdf.rect(10 * mm, 98 * mm, 2 * mm, 2 * mm)
        #     pdf.drawString(15 * mm, 100 * mm, billet.moine5.__str__())
        pdf.saveState()

        # Divers (prix, chauffeur, remarques):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(10 * mm, 106 * mm, 'Remarques')
        pdf.roundRect(7 * mm, 108 * mm, width - 2 * 7 * mm, 35 * mm, 3 * mm)
        pdf.restoreState()
        # Prix :
        prix = 'Prix :'
        if billet.gratis:
            prix += ' - Gratis pro Deo.'
        elif billet.prix:
            prix += str(billet.prix) + ' €'
            prix += ' (facture)' if billet.facture else ''
        prix += ' - Apporter la carte vitale' if billet.vitale else ''
        pdf.drawString(10 * mm, 113 * mm, prix)
        # Chauffeur :
        if billet.chauffeur:
            pdf.drawString(10 * mm, 118 * mm, 'Chauffeur : ' +
                           billet.chauffeur.__str__())
        # Remarques :
        if billet.remarque:
            pdf.drawString(10 * mm, 123 * mm, billet.remarque)

        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer, filename='billet.pdf')
