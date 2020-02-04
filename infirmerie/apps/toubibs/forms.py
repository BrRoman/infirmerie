""" apps/toubibs/forms.py """

from django import forms

from .models import Toubib


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
    specialite = forms.ChoiceField(
        label='Spécialité :',
        choices=[
            ('Généraliste', 'Généraliste'),
            ('Acupuncteur', 'Acupuncteur'),
            ('Chirurgien', 'Chirurgien'),
            ('Dentiste', 'Dentiste'),
            ('Gérontologue ', 'Gérontologue'),
            ('Ophtalmo', 'Ophtalmo'),
            ('Gastro', 'Gastro'),
            ('Homéopathe', 'Homéopathe'),
            ('Infirmier(ère)', 'Infirmier(ère)'),
            ('Kiné', 'Kiné'),
            ('Naturopathe', 'Naturopathe'),
            ('Neurologue', 'Neurologue'),
            ('ORL', 'ORL'),
            ('Pharmacie', 'Pharmacie'),
            ('Phlébologue', 'Phlébologue'),
            ('Podologue', 'Podologue'),
            ('Psychiatre', 'Psychiatre'),
            ('Psychothérapeute', 'Psychothérapeute'),
            ('Rhumato', 'Rhumato'),
            ('Urologue', 'Urologue'),
        ],
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

    class Meta:
        model = Toubib
        fields = ['titre', 'nom', 'prenom', 'specialite', 'adresse_1', 'adresse_2',
                  'adresse_3', 'code_postal', 'ville', 'telephone', 'email']
