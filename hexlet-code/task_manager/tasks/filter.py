import django_filters
from django import forms
from task_manager.tasks.models import Task
from django.contrib.auth.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.contrib import messages

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(label='Статус', queryset=Status.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    executor = django_filters.ModelChoiceFilter(label='Исполнитель', queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    labels = django_filters.ModelChoiceFilter(label='Метка', queryset=Label.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    
    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.dict().get('self_tasks', None) == 'on':
            author = getattr(self.request, 'user', None)
            return parent.filter(author=author)
        return parent