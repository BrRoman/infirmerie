""" apps/moines/forms.py """

from django import forms
from tempus_dominus.widgets import DatePicker

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
    date_naissance = forms.DateField(
        label='Date de naissance :',
        widget=DatePicker(),
    )

    class Meta:
        model = Moine
        fields = ['titre', 'nom_religieux',
                  'prenom_civil', 'nom_civil', 'date_naissance']
