""" apps/main/views.py """

import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.moines.models import Moine


class HomeView(LoginRequiredMixin, TemplateView):
    """ Home view. """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moines_dentiste'] = Moine.objects.filter(
            date_dentiste__lt=datetime.datetime.today() - datetime.timedelta(days=365))
        return context
