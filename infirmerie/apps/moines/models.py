""" apps/moines/models.py """

from django.db import models
from django.urls import reverse

from apps.toubibs.models import Toubib


class Moine(models.Model):
    """ Moine model. """
    titre = models.CharField(
        max_length=25,
    )
    nom_religieux = models.CharField(
        max_length=255,
    )
    is_chauffeur = models.BooleanField(
        default=False,
    )
    prenom_civil = models.CharField(
        max_length=255,
    )
    nom_civil = models.CharField(
        max_length=255,
    )
    numero_secu = models.CharField(
        max_length=15,
        null=True,
    )
    date_naissance = models.DateField(
        null=True,
    )
    medecin_traitant = models.ForeignKey(
        null=True,
        to=Toubib,
        on_delete=models.SET_NULL,
        related_name='medecin_traitant',
    )
    dentiste = models.ForeignKey(
        null=True,
        to=Toubib,
        on_delete=models.SET_NULL,
        related_name='dentiste',
    )
    date_vaccin = models.DateField(
        null=True,
    )
    date_dentiste = models.DateField(
        null=True,
    )
    date_ophtalmo = models.DateField(
        null=True,
    )
    date_don_sang = models.DateField(
        null=True,
    )
    date_prostate = models.DateField(
        null=True,
    )
    date_hemocult = models.DateField(
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        nom_complet = ''
        nom_complet += self.titre + ' ' if self.titre != 'Postulant' else ''
        nom_complet += self.nom_religieux if self.nom_religieux else (
            self.prenom_civil + ' ' + self.nom_civil.upper())
        nom_complet += ' Marie' if self.nom_religieux else ''
        return nom_complet

    def civil(self):
        """ Return the complete civil name of the monk. """
        if self.titre == 'Postulant':
            return ''
        civil = ''
        civil += self.prenom_civil if self.prenom_civil else ''
        civil += ' ' if self.prenom_civil else ''
        civil += self.nom_civil.upper() if self.nom_civil else ''
        return civil

    def get_absolute_url(self):
        """ Return absolute url. """
        return reverse('moines:detail', args=[self.pk])
