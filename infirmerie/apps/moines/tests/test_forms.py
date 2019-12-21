""" apps/moines/tests/tests_forms.py """

import datetime

from django.test import TestCase

from .. import forms


class MoinesFormTest(TestCase):
    """ Test Moine form. """

    def setUp(self):
        self.valid_data = {
            'titre': 'Fr.',
            'nom_religieux': 'aaa',
            'prenom_civil': 'bbb',
            'nom_civil': 'ccc',
            'date_naissance': datetime.date.today() - datetime.timedelta(days=365),
            'date_vaccin': datetime.date.today() - datetime.timedelta(days=30),
            'date_dentiste': datetime.date.today() - datetime.timedelta(days=30),
        }

    # Date naissance :
    def test_date_naissance_in_past(self):
        """ Date naissance in the past is valid. """
        form = forms.MoineForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_date_naissance_in_future(self):
        """ Date naissance in the future is invalid. """
        data = self.valid_data
        date_test = datetime.date.today() + datetime.timedelta(days=365)
        data['date_naissance'] = date_test
        form = forms.MoineForm(data=data)
        self.assertFalse(form.is_valid())

    # Date vaccin :
    def test_date_vaccin_in_past(self):
        """ Date vaccin in the past is valid. """
        form = forms.MoineForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_date_vaccin_in_future(self):
        """ Date vaccin in the future is invalid. """
        data = self.valid_data
        date_test = datetime.date.today() + datetime.timedelta(days=365)
        data['date_vaccin'] = date_test
        form = forms.MoineForm(data=data)
        self.assertFalse(form.is_valid())

    # Date dentiste :
    def test_date_dentiste_in_past(self):
        """ Date dentiste in the past is valid. """
        form = forms.MoineForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_date_dentiste_in_future(self):
        """ Date dentiste in the future is invalid. """
        data = self.valid_data
        date_test = datetime.date.today() + datetime.timedelta(days=365)
        data['date_dentiste'] = date_test
        form = forms.MoineForm(data=data)
        self.assertFalse(form.is_valid())
