"""Forms of the project."""
from django import forms
from .models import Thing


class ThingForm(forms.Form):
    model = Thing

    fields = ['name', 'description', 'quantity']
    widgets = {'description' : forms.Textarea(),
               'quantity' : forms.NumberInput()}
