from django.db import models
from django.contrib.auth.models import User

PERE = 'Père'
FRERE = 'Frère'
DOCTEUR = 'Docteur'
MONSIEUR = 'Monsieur'
MADAME = 'Madame'


class Moine(models.Model):
    titre = models.CharField(
        max_length=5,
        choices=[
            (PERE, 'P. '),
            (FRERE, 'Fr. '),
        ]
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
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.titre + " " if self.titre != "" else "") + self.nom_religieux


class Toubib(models.Model):
    titre = models.CharField(
        max_length=20,
        choices=[
            (DOCTEUR, 'Docteur'),
            (MONSIEUR, 'Monsieur'),
            (MADAME, 'Madame'),
        ]
    )
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    adresse_rue_1 = models.CharField(max_length=255)
    adresse_rue_2 = models.CharField(max_length=255)
    adresse_rue_3 = models.CharField(max_length=255)
    adresse_code = models.CharField(max_length=10)
    adresse_ville = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre + (" " if self.titre != "" else "") + self.prenom + (" " if self.titre != "" else "") + self.nom


class Billet(models.Model):
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
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
