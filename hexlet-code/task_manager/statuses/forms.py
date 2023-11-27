from django import forms
from task_manager.statuses import models

class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = models.Status
        fields = ['name']
        
class StatusUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = models.Status
        fields = ['name']