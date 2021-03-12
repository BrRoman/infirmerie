""" apps/billets/models.py """

from django.db import models

from apps.moines.models import Moine
from apps.toubibs.models import Toubib


class Billet(models.Model):
    """ Billet model. """
    titre = models.CharField(
        max_length=255,
    )
    moine1 = models.ForeignKey(
        Moine,
        related_name='billets_moine1',
        on_delete=models.CASCADE,
    )
    moine2 = models.ForeignKey(
        Moine,
        related_name='billets_moine2',
        on_delete=models.CASCADE,
        null=True,
    )
    moine3 = models.ForeignKey(
        Moine,
        related_name='billets_moine3',
        on_delete=models.CASCADE,
        null=True,
    )
    moine4 = models.ForeignKey(
        Moine,
        related_name='billets_moine4',
        on_delete=models.CASCADE,
        null=True,
    )
    chauffeur = models.ForeignKey(
        Moine,
        related_name='billets_chauffeur',
        on_delete=models.CASCADE,
        null=True,
    )
    toubib = models.ForeignKey(
        Toubib,
        related_name='billets_toubib',
        on_delete=models.CASCADE,
    )
    when = models.DateTimeField()
    where = models.CharField(
        max_length=25,
    )
    prix = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,
    )
    facture = models.BooleanField(
        default=False,
    )
    gratis = models.BooleanField(
        default=False,
    )
    vitale = models.BooleanField(
        default=False,
    )
    remarque = models.TextField(
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

    def moines(self):
        """ Return a unique string of all the monks. """
        moines = ''
        moines += self.moine1.__str__()
        moines += (', ' + self.moine2.__str__()) if self.moine2 else ''
        moines += (', ' + self.moine3.__str__()) if self.moine3 else ''
        moines += (', ' + self.moine4.__str__()) if self.moine4 else ''
        return moines

    def date_time(self):
        """ Return date and time of rendez-vous under human form. """
        return self.when.strftime('%d/%m/%Y') + ' à ' + self.when.strftime('%H:%M')
