from django.shortcuts import render
from django.views import View
from task_manager.statuses import models
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin

# Create your views here.
class IndexViewStatuses(AccessMixin, View):
    def get(self, request, *args, **kwargs):
        statuses = models.Status.objects.all()
        return render(request, 'statuses/index.html', {'statuses': statuses})
    
class CreateViewStatus(AccessMixin, SuccessMessageMixin, CreateView):
    form_class = forms.StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:index')
    login_url = reverse_lazy('statuses:create')
    success_message = 'Статус успешно создан'
    
class UpdateViewStatus(AccessMixin, SuccessMessageMixin, UpdateView):
    model = models.Status
    form_class = forms.StatusUpdateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:index')
    login_url = reverse_lazy('statuses:update')
    success_message = 'Статус успешно обновлен'
    
class DeleteViewStatus(AccessMixin, SuccessMessageMixin, DeleteView):
    model = models.Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:index')
    success_message = 'Status deleted'
    login_url = reverse_lazy('statuses:delete')