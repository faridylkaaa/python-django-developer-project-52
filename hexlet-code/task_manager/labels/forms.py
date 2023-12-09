from django import forms
from task_manager.labels.models import Label

class CreateFormLabel(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))    

    class Meta:
        model = Label
        fields = ['name']