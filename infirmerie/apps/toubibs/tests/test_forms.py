""" apps/toubibs/tests/tests_forms.py """

from django.test import TestCase

from .. import forms


class ToubibsFormTest(TestCase):
    """ Test Toubib form. """

    def setUp(self):
        self.valid_data = {
            'titre': 'Dr',
            'prenom': 'aaa',
            'nom': 'bbb',
        }

    def test_titre_in_available_values(self):
        """ Test form with titre out of available values is invalid. """
        data = self.valid_data
        data['titre'] = 'xxx'
        form = forms.ToubibForm(data=data)
        self.assertFalse(form.is_valid())
