""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import InfirmerieLoginForm


class InfirmerieLoginView(LoginView):
    """ Login view. """
    form_class = InfirmerieLoginForm
    template_name = 'accounts/login.html'
