""" apps/moines/tests/tests_models.py """

from django.test import TestCase
from django.urls import reverse

from ..models import Moine


class MoinesModelsTests(TestCase):
    """ Tests Moines Models. """

    def setUp(self):
        self.moine_test = Moine.objects.create(nom_religieux='Test')

    def test_get_absolute_url(self):
        """ Return absolute url. """
        author = Moine.objects.get(id=self.moine_test.pk)
        self.assertEqual(author.get_absolute_url(), reverse(
            'moines:detail', args=[self.moine_test.pk]))
