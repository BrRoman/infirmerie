""" apps/moines/models.py """

from django.db import models
from django.urls import reverse


class Moine(models.Model):
    """ Moine model. """
    titre = models.CharField(
        max_length=25,
    )
    nom_religieux = models.CharField(
        max_length=255,
    )
    prenom_civil = models.CharField(
        max_length=255,
    )
    nom_civil = models.CharField(
        max_length=255,
    )
    date_naissance = models.DateField(
        null=True,
    )
    date_vaccin = models.DateField(
        null=True,
    )
    date_dentiste = models.DateField(
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
        nom_complet += self.titre + ' ' if self.titre != '-' else ''
        nom_complet += self.nom_religieux if self.nom_religieux != '' else (
            self.prenom_civil + ' ' + self.nom_civil)
        nom_complet += ' Marie' if self.nom_religieux != '' else ''
        return nom_complet

    def get_absolute_url(self):
        """ Return absolute url. """
        return reverse('moines:detail', args=[self.pk])
