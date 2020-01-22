""" apps/billets/forms.py """

from django import forms

from tempus_dominus.widgets import DateTimePicker

from apps.moines.models import Moine
from apps.toubibs.models import Toubib
from .models import Billet


class BilletForm(forms.ModelForm):
    """ Billet form. """
    titre = forms.CharField(
        max_length=255,
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        help_text='Par exemple "P. Vianney (ophtalmo)"',
    )
    when = forms.DateTimeField(
        label='Date et heure :',
        input_formats=[
            '%d/%m/%Y %H:%M',
        ],
        widget=DateTimePicker(
            options={
                'format': 'DD/MM/YYYY HH:mm',
                'locale': 'fr',
                'sideBySide': True,
            },
        ),
        error_messages={
            'invalid': 'Date invalide.',
            'required': 'Ce champ est obligatoire',
        }
    )
    where = forms.ChoiceField(
        choices=[
            ('Travail', 'Travail'),
            ('Domicile', 'Domicile'),
            ('Infirmerie', 'Infirmerie'),
            ('Porterie', 'Porterie'),
        ],
        label='Lieu :',
    )
    moine1 = forms.ModelChoiceField(
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine 1 :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    moine2 = forms.ModelChoiceField(
        required=False,
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine 2 :',
    )
    moine3 = forms.ModelChoiceField(
        required=False,
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine 3 :',
    )
    moine4 = forms.ModelChoiceField(
        required=False,
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine 4 :',
    )
    moine5 = forms.ModelChoiceField(
        required=False,
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine 5 :',
    )
    chauffeur = forms.ModelChoiceField(
        required=False,
        queryset=Moine.objects.filter(
            is_chauffeur=True).order_by('nom_religieux'),
        label='Chauffeur :',
    )
    prix = forms.FloatField(
        required=False,
        label='Prix :',
        widget=forms.TextInput,
        help_text='NB : Les éventuelles virgules sont automatiquement converties en points.',
    )
    facture = forms.BooleanField(
        required=False,
        label='Facture',
        label_suffix='',
    )
    gratis = forms.BooleanField(
        required=False,
        label='Gratis',
        label_suffix='',
    )
    vitale = forms.BooleanField(
        required=False,
        label='Carte vitale',
        label_suffix='',
    )
    toubib = forms.ModelChoiceField(
        queryset=Toubib.objects.all().order_by('nom'),
        label='Toubib :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    remarque = forms.CharField(
        required=False,
        label='Remarques :',
        widget=forms.Textarea,
    )

    class Meta:
        model = Billet
        fields = ('titre', 'when', 'where', 'moine1', 'moine2', 'moine3',
                  'moine4', 'moine5', 'chauffeur', 'prix', 'facture', 'gratis', 'vitale', 'toubib', 'remarque')
