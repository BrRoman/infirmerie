""" apps/toubibs/forms.py """

from django import forms

from .models import Speciality, Toubib


class ToubibForm(forms.ModelForm):
    """ Toubib form. """
    titre = forms.ChoiceField(
        label='Qualité :',
        choices=[
            ('Dr', 'Docteur'),
            ('M.', 'Monsieur'),
            ('Mme', 'Madame'),
        ],
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    nom = forms.CharField(
        label='Nom :',
        error_messages={
            'required': 'Ce champ est obligatoire.',
        }
    )
    prenom = forms.CharField(
        required=False,
        label='Prénom :',
    )
    speciality = forms.ModelChoiceField(
        label='Spécialité :',
        queryset=Speciality.objects.all().order_by('speciality'),
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    is_medecin = forms.BooleanField(
        required=False,
        label='Est médecin',
        label_suffix='',
    )
    adresse_1 = forms.CharField(
        required=False,
        label='Adresse 1 :',
    )
    adresse_2 = forms.CharField(
        required=False,
        label='Adresse 2 :',
    )
    adresse_3 = forms.CharField(
        required=False,
        label='Adresse 3 :',
    )
    code_postal = forms.CharField(
        required=False,
        label='Code postal :',
    )
    ville = forms.CharField(
        required=False,
        label='Ville :',
    )
    telephone = forms.CharField(
        required=False,
        label='Téléphone :',
    )
    email = forms.EmailField(
        required=False,
        label='Mail :',
        error_messages={
            'invalid': 'Adresse mail invalide.',
        }
    )
    remarques = forms.CharField(
        required=False,
        label='Remarques',
        widget=forms.Textarea,
    )

    class Meta:
        model = Toubib
        fields = ['titre', 'nom', 'prenom', 'speciality', 'is_medecin', 'adresse_1', 'adresse_2',
                  'adresse_3', 'code_postal', 'ville', 'telephone', 'email', 'remarques']


class SpecialityForm(forms.ModelForm):
    """ Form for speciality. """
    speciality = forms.CharField(
        label='Nom de la spécialité :',
        label_suffix='',
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )

    class Meta:
        model = Speciality
        fields = ['speciality']
