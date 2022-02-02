from django import forms
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(label='URL', widget=forms.URLInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Shorten your link'}))

    class Meta:
        model = Shortener
        fields = ('long_url',)
