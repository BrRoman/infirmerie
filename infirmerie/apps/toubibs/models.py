from django.db import models

DOCTEUR = 'Docteur'
MONSIEUR = 'Monsieur'
MADAME = 'Madame'


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
