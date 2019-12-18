""" apps/moines/forms.py """

from django import forms

from .models import Moine


POSTULANT = ''
FRERE = 'Frère'
PERE = 'Père'


class MoineForm(forms.ModelForm):
    """ Moine form. """
    titre = forms.ChoiceField(
        label='Qualité :',
        choices=[
            (POSTULANT, 'Postulant'),
            (FRERE, 'Fr. '),
            (PERE, 'P. '),
        ],
    )
    nom_religieux = forms.CharField(
        label='Nom religieux :',
    )
    prenom_civil = forms.CharField(
        label='Prénom civil :',
    )
    nom_civil = forms.CharField(
        label='Nom civil :',
    )

    class Meta:
        model = Moine
        fields = ['titre', 'nom_religieux', 'prenom_civil', 'nom_civil']
