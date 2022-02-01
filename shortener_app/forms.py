from django import forms
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(label='URL', widget=forms.URLInput())

    class Meta:
        model = Shortener
        fields = ('long_url',)
