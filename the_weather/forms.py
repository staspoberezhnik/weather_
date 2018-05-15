from django.forms import ModelForm, TextInput, Form
from .models import ExistCity, NewCity
from django import forms


class SelectCityForm(ModelForm):
    class Meta:
        model = ExistCity
        fields = ['name']

    CITY_CHOICES = (
        ('London', 'London'),
        ('Tokyo', 'Tokyo'),
        ('New York', 'New York'),
        ('Liverpool', 'Liverpool'),
        ('Kyiv', 'Kyiv'),
        ('Vinnytsia', 'Vinnytsia'),
        ('Las Vegas', 'Las Vegas'),
        ('Donetsk', 'Donetsk'),
        ('Lviv', 'Lviv'),
        ('Baku', 'Baku'),
        ('Moscow', 'Moscow'),
        ('Sevastopol', 'Sevastopol'),
        ('Paris', 'Paris'),
    )
    name = forms.ChoiceField(choices=CITY_CHOICES, label="", initial='', widget=forms.Select(), required=False)
    widgets = {'name': TextInput(attrs={'class': 'select', 'placeholder': 'Input City name'})}


class InputCityForm(ModelForm):
    class Meta:
        model = NewCity
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'select', 'placeholder': 'Input City name'})}

