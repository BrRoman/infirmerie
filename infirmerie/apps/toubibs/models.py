""" apps/toubibs/models.py """

from django.db import models
from django.urls import reverse


class Speciality(models.Model):
    """ Speciality model. """
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.speciality

    class Meta:
        verbose_name_plural = 'specialities'


class Toubib(models.Model):
    """ Toubib model. """
    titre = models.CharField(max_length=25)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    nom = models.CharField(max_length=50)
    specialite = models.CharField(max_length=25)
    speciality = models.ForeignKey(
        to=Speciality,
        on_delete=models.CASCADE,
    )
    adresse_1 = models.CharField(max_length=255, null=True, blank=True)
    adresse_2 = models.CharField(max_length=255, null=True, blank=True)
    adresse_3 = models.CharField(max_length=255, null=True, blank=True)
    code_postal = models.CharField(max_length=10, null=True, blank=True)
    ville = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    remarques = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        nom_complet = self.titre
        nom_complet += ' ' if self.titre else ''
        nom_complet += self.prenom if self.prenom else ''
        nom_complet += ' ' if self.prenom else ''
        nom_complet += self.nom.upper()
        return nom_complet

    def get_absolute_url(self):
        """ Return absolute url. """
        return reverse('toubibs:detail', args=[self.pk])

    def adresse_complete(self):
        """ Return complete address as text. """
        adresse_complete = ''
        adresse_complete += self.adresse_1 if self.adresse_1 else ''
        adresse_complete += '\n' if self.adresse_1 else '' + \
            self.adresse_2 if self.adresse_2 else ''
        adresse_complete += '\n' if self.adresse_2 else '' + \
            self.adresse_3 if self.adresse_3 else ''
        adresse_complete += '\n' if self.adresse_3 else '' + \
            self.code_postal if self.code_postal else ''
        adresse_complete += ' ' if self.code_postal else ''
        adresse_complete += self.ville if self.ville else ''
        return adresse_complete
