""" apps/billets/models.py """

from django.db import models

from apps.moines.models import Moine
from apps.toubibs.models import Toubib


class Billet(models.Model):
    """ Billet model. """
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
        when = self.when
        return when.strftime('%d/%m/%Y') + ' à ' + when.strftime('%H:%M')
