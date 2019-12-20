""" apps/moines/forms.py """

from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Moine


class MoineForm(forms.ModelForm):
    """ Moine form. """
    titre = forms.ChoiceField(
        label='Qualité :',
        choices=[
            ('-', 'Postulant'),
            ('Fr.', 'Frère'),
            ('P.', 'Père'),
        ],
    )
    nom_religieux = forms.CharField(
        required=False,
        label='Nom religieux :',
        help_text='NB : "Marie" sera ajouté automatiquement.'
    )
    prenom_civil = forms.CharField(
        label='Prénom civil :',
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    nom_civil = forms.CharField(
        label='Nom civil :',
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    date_naissance = forms.DateField(
        required=False,
        label='Date de naissance :',
        widget=DatePicker(),
    )
    date_vaccin = forms.DateField(
        required=False,
        label='Date du dernier vaccin :',
        widget=DatePicker(),
    )
    date_dentiste = forms.DateField(
        required=False,
        label='Dernier rendez-vous dentiste :',
        widget=DatePicker(),
    )

    class Meta:
        model = Moine
        fields = ['titre', 'nom_religieux',
                  'prenom_civil', 'nom_civil', 'date_naissance', 'date_vaccin', 'date_dentiste']
