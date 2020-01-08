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
    moine = forms.ModelChoiceField(
        queryset=Moine.objects.all().order_by('nom_religieux'),
        label='Moine :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )
    toubib = forms.ModelChoiceField(
        queryset=Toubib.objects.all().order_by('nom'),
        label='Toubib :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
    )

    class Meta:
        model = Billet
        fields = ('titre', 'when', 'moine', 'toubib')
