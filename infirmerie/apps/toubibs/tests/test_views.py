""" apps/toubibs/tests/tests_views.py """

from urllib.parse import quote

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import resolve, reverse

from ..models import Toubib
from .. import views


class ToubibsViewsTests(TestCase):
    """ Test Toubibs views. """

    def setUp(self):
        self.testuser = User.objects.create_superuser(username='testuser')
        self.client = Client()
        self.toubib_test = Toubib.objects.create(titre='Dr', nom='Test')

    # List:
    def test_list_redirect_if_no_login(self):
        """ List view redirects if no login. """
        url = reverse('toubibs:list', args=[1])
        response = self.client.get(url)
        self.assertRedirects(
            response, '/accounts/login?next=' + quote(quote(url)))

    def test_list_200(self):
        """ List view returns 200 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:list', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_404(self):
        """ List view returns 404 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:list', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_list_url_resolves_list_view(self):
        """ List url resolves to list view. """
        self.client.force_login(self.testuser)
        view = resolve('/toubibs/page=1')
        self.assertEqual(view.func.__name__,
                         views.ToubibListView.as_view().__name__)

    def test_list_view_contains_links_to_toubibs(self):
        """ List view contains links to toubib."""
        self.client.force_login(self.testuser)
        toubib_url = reverse('toubibs:detail', args=[self.toubib_test.pk])
        response = self.client.get('/toubibs/page=1')
        self.assertContains(response, 'href={0}'.format(toubib_url))

    # Create:
    def test_create_redirect_if_no_login(self):
        """ Create view redirects if no login. """
        url = reverse('toubibs:create')
        response = self.client.get(url)
        self.assertRedirects(
            response, '/accounts/login?next=' + quote(quote(url)))

    def test_create_200(self):
        """ Create view returns 200 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_url_resolves_create_view(self):
        """ Create url resolves to create view. """
        self.client.force_login(self.testuser)
        view = resolve('/toubibs/create')
        self.assertEqual(view.func.__name__,
                         views.ToubibCreateView.as_view().__name__)

    # Detail:
    def test_detail_redirect_if_no_login(self):
        """ Detail view redirects if no login. """
        url = reverse('toubibs:detail', args=[self.toubib_test.pk])
        response = self.client.get(url)
        self.assertRedirects(
            response, '/accounts/login?next=' + quote(quote(url)))

    def test_detail_200(self):
        """ Detail view returns 200 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:detail', args=[self.toubib_test.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_404(self):
        """ Detail view returns 404 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_url_resolves_detail_view(self):
        """ Detail url resolves to detail view. """
        self.client.force_login(self.testuser)
        view = resolve('/toubibs/id=1/detail')
        self.assertEqual(view.func.__name__,
                         views.ToubibDetailView.as_view().__name__)

    # Update:
    def test_update_redirect_if_no_login(self):
        """ Update view redirects if no login. """
        url = reverse('toubibs:update', args=[self.toubib_test.pk])
        response = self.client.get(url)
        self.assertRedirects(
            response, '/accounts/login?next=' + quote(quote(url)))

    def test_update_200(self):
        """ Update view returns 200 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:update', args=[self.toubib_test.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_404(self):
        """ Update view returns 404 code. """
        self.client.force_login(self.testuser)
        url = reverse('toubibs:update', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_update_url_resolves_update_view(self):
        """ Update url resoves to update view. """
        self.client.force_login(self.testuser)
        view = resolve('/toubibs/id=1/update')
        self.assertEqual(view.func.__name__,
                         views.ToubibUpdateView.as_view().__name__)
