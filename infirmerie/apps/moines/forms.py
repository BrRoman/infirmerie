""" apps/moines/forms.py """

import datetime

from django import forms

from tempus_dominus.widgets import DatePicker

from apps.toubibs.models import Toubib
from .models import Moine


class MoineForm(forms.ModelForm):
    """ Moine form. """
    titre = forms.ChoiceField(
        label='Qualité :',
        choices=[
            ('Postulant', 'Postulant'),
            ('Fr.', 'Frère'),
            ('P.', 'Père'),
        ],
    )
    nom_religieux = forms.CharField(
        required=False,
        label='Nom religieux :',
        help_text='NB : "Marie" sera ajouté automatiquement.'
    )
    is_chauffeur = forms.BooleanField(
        required=False,
        label='Peut conduire',
        label_suffix='',
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
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'fr',
            }
        ),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    numero_secu = forms.CharField(
        required=False,
        max_length=15,
        min_length=15,
        help_text='15 caractères, sans espace',
        label='Numéro de sécurité sociale',
    )
    medecin_traitant = forms.ModelChoiceField(
        required=False,
        queryset=Toubib.objects.filter(
            specialite='Généraliste').order_by('nom', 'prenom'),
        label='Médecin traitant',
    )
    dentiste = forms.ModelChoiceField(
        required=False,
        queryset=Toubib.objects.filter(
            specialite='Dentiste').order_by('nom', 'prenom'),
        label='Dentiste',
    )
    date_vaccin = forms.DateField(
        required=False,
        label='Date du dernier vaccin :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    date_dentiste = forms.DateField(
        required=False,
        label='Dernier rendez-vous dentiste :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    date_ophtalmo = forms.DateField(
        required=False,
        label='Dernier rendez-vous ophtalmo :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    date_don_sang = forms.DateField(
        required=False,
        label='Dernier don du sang :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    date_prostate = forms.DateField(
        required=False,
        label='Dernier examen prostate :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    date_hemocult = forms.DateField(
        required=False,
        label='Dernier examen hémocult :',
        input_formats=[
            '%d/%m/%Y',
        ],
        widget=DatePicker(options={
            'format': 'DD/MM/YYYY',
        }),
        error_messages={
            'invalid': 'Date invalide.',
        }
    )
    remarques = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        model = Moine
        fields = ['titre', 'nom_religieux', 'is_chauffeur',
                  'prenom_civil', 'nom_civil', 'date_naissance', 'numero_secu', 'medecin_traitant', 'dentiste', 'date_vaccin', 'date_dentiste', 'date_ophtalmo', 'date_don_sang', 'date_prostate', 'date_hemocult', 'remarques']

    def clean_date_naissance(self):
        """ Check date naissance in the past. """
        date_naissance = self.cleaned_data['date_naissance']
        if date_naissance and date_naissance > datetime.date.today():
            raise forms.ValidationError(
                'Date de naissance dans le futur !', code='invalid')
        return date_naissance

    def clean_date_vaccin(self):
        """ Check date vaccin in the past. """
        date_vaccin = self.cleaned_data['date_vaccin']
        if date_vaccin and date_vaccin > datetime.date.today():
            raise forms.ValidationError(
                'Date de vaccin dans le futur !', code='invalid')
        return date_vaccin

    def clean_date_dentiste(self):
        """ Check date dentiste in the past. """
        date_dentiste = self.cleaned_data['date_dentiste']
        if date_dentiste and date_dentiste > datetime.date.today():
            raise forms.ValidationError(
                'Date de dentiste dans le futur !', code='invalid')
        return date_dentiste
