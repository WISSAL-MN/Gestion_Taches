from django import forms
from .models import Task

class TacheForm(forms.ModelForm):
    tache = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Enter la tache',
        'class': 'form-control form-control-lg'
    }))
    class Meta:
        model = Task
        fields = [
            'tache'
        ]