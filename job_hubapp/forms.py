from django import forms

class MyFileForm(forms.Form):
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))