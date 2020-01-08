""" apps/billets/models.py """

from django.db import models

from apps.moines.models import Moine
from apps.toubibs.models import Toubib


class Billet(models.Model):
    """ Billet model. """
    titre = models.CharField(
        max_length=255,
    )
    moine = models.ForeignKey(
        Moine,
        related_name='billets',
        on_delete=models.CASCADE
    )
    toubib = models.ForeignKey(
        Toubib,
        related_name='billets',
        on_delete=models.CASCADE
    )
    when = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

    def date_time(self):
        """ Return date and time of rendez-vous under human form. """
        return self.when.strftime('%d/%m/%Y') + ' à ' + self.when.strftime('%H:%M')
