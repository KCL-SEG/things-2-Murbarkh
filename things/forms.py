"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator


class ThingForm(forms.Form):
    model = Thing

    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120, widget=forms.Textarea())
    quantity = forms.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)],
        widget=forms.NumberInput()
    )


