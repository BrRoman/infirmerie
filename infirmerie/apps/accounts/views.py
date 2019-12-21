""" apps/accounts/views.py """

from django.shortcuts import render


def login(request):
    """ Login view. """
    return render(request, 'accounts/login.html')
