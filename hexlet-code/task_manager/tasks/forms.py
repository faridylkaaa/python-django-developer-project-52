from django import forms
from task_manager.tasks.models import Task
from task_manager.statuses import models
from django.contrib.auth.models import User
from task_manager.labels.models import Label

class CreateTaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    status = forms.ModelChoiceField(label='Cтатус', queryset=models.Status.objects, widget=forms.Select(attrs={'class': 'form-select'}))
    executor = forms.ModelChoiceField(label='Испольнитель', queryset=User.objects, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    labels = forms.ModelMultipleChoiceField(label='labels', queryset=Label.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-select'}), required=False)
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'executor': forms.Select(attrs={'class': 'form-select'})
        }
        
class UpdateTaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    status = forms.ModelChoiceField(label='Cтатус', queryset=models.Status.objects, widget=forms.Select(attrs={'class': 'form-select'}))
    executor = forms.ModelChoiceField(label='Испольнитель', queryset=User.objects, widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    labels = forms.ModelMultipleChoiceField(label='labels', queryset=Label.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-select'}), required=False)

    
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']