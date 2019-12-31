""" apps/toubibs/tests/tests_models.py """

from django.test import TestCase
from django.urls import reverse

from ..models import Toubib


class ToubibsModelsTests(TestCase):
    """ Tests Toubibs Models. """

    def setUp(self):
        self.toubib_test = Toubib.objects.create(titre='Dr', nom='Test')

    def test_get_absolute_url(self):
        """ Return absolute url. """
        author = Toubib.objects.get(id=self.toubib_test.pk)
        self.assertEqual(author.get_absolute_url(), reverse(
            'toubibs:detail', args=[self.toubib_test.pk]))
