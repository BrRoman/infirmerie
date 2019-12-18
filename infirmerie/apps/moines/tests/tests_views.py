""" apps/moines/tests/tests_views.py """

from django.urls import resolve, reverse
from django.test import TestCase

from ..models import Moine
from .. import views


class MoinesViewsTests(TestCase):
    """ Test Moines views. """

    def setUp(self):
        self.moine_test = Moine.objects.create(nom_religieux='Test')

    # List:
    def test_list_view_status_code(self):
        """ List view returns 200 code. """
        url = reverse('moines:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_url_resolves_list_view(self):
        """ List url resolves to list view. """
        view = resolve('/moines/')
        self.assertEqual(view.func.__name__,
                         views.MoineListView.as_view().__name__)

    def test_list_view_contains_links_to_moines(self):
        """ List view contains links to moine."""
        moine_url = reverse('moines:detail', kwargs={'pk': self.moine_test.pk})
        response = self.client.get('/moines/')
        self.assertContains(response, 'href="{0}"'.format(moine_url))

    # Create:
    def test_create_view_status_code(self):
        """ Create view returns 200 code. """
        url = reverse('moines:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_url_resolves_create_view(self):
        """ Create url resolves to create view. """
        view = resolve('/moines/create')
        self.assertEqual(view.func.__name__,
                         views.MoineCreateView.as_view().__name__)

    # Detail:
    def test_detail_200(self):
        """ Detail view returns 200 code. """
        url = reverse('moines:detail', kwargs={'pk': self.moine_test.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_404(self):
        """ Detail view returns 404 code. """
        url = reverse('moines:detail', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_url_resolves_detail_view(self):
        """ Detail url resolves to detail view. """
        view = resolve('/moines/1/detail')
        self.assertEqual(view.func.__name__,
                         views.MoineDetailView.as_view().__name__)

    # Update:
    def test_update_200(self):
        """ Update view returns 200 code. """
        url = reverse('moines:update', kwargs={'pk': self.moine_test.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_404(self):
        """ Update view returns 404 code. """
        url = reverse('moines:update', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_update_url_resolves_update_view(self):
        """ Update url resoves to update view. """
        view = resolve('/moines/1/update')
        self.assertEqual(view.func.__name__,
                         views.MoineUpdateView.as_view().__name__)
