from django.db import models

PERE = 'Père'
FRERE = 'Frère'


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
