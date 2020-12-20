""" apps/toubibs/forms.py """

from django import forms

from .models import Specialities, Toubib


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
    specialite = forms.ModelChoiceField(
        label='Spécialité :',
        queryset=Specialities.objects.all().order_by('speciality'),
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
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
        fields = ['titre', 'nom', 'prenom', 'specialite', 'adresse_1', 'adresse_2',
                  'adresse_3', 'code_postal', 'ville', 'telephone', 'email', 'remarques']
