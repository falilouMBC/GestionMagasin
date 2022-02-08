from django import forms
from django.conf import settings


class PersonForm(forms.Form):
    name = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    age = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )
    )

    sex = forms.ChoiceField(
        required = True,
        choices = [(x, y) for (x, y) in settings.SEXE],
        widget = forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    country = forms.ChoiceField(
        required = True,
        choices = [(x, y) for (x, y) in settings.COUNTRIES],
        widget = forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
class MagasinForm(forms.Form):

    # name2 = forms.CharField(
    #     widget= forms.TextInput()
    #     # attrs pour pouvoir mettre des attributs
    # )

    # name3 = forms.CharField(
    #     widget=forms.NumberInput()
    # )

    # name4 = forms.ChoiceField(
    #     widget = forms.RadioSelect
    # )

    # name5 = forms.FileField(
    #     widget = forms.FileInput()
    # )

    # name8 = forms.CharField(
    #     widget = forms.PasswordInput()
        
    # )
        name = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
        prix = forms.CharField(
        required = True,
        max_length = 200,
        strip = True,
        min_length = 2,
        widget = forms.NumberInput(
            attrs={
                'type': 'decimal'
            }
        )
        
    )
        country = forms.ChoiceField(
        required = True,
        choices = [(x, y) for (x, y) in settings.COUNTRIES],
        widget = forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    