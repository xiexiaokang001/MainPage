from django import forms

class AsciiFrom(forms.Form):
    input = forms.CharField()