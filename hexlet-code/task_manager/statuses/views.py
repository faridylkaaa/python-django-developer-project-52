from django.shortcuts import render
from django.views import View
from task_manager.statuses import models
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.statuses import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexViewStatuses(LoginRequiredMixin, View):
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    
    def get(self, request, *args, **kwargs):
        statuses = models.Status.objects.all()
        return render(request, 'statuses/index.html', {'statuses': statuses})
    
class CreateViewStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.StatusCreateForm
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:index')
    login_url = reverse_lazy('statuses:create')
    success_message = 'Статус успешно создан'
    
class UpdateViewStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = models.Status
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    form_class = forms.StatusUpdateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:index')
    login_url = reverse_lazy('statuses:update')
    success_message = 'Статус успешно обновлен'
    
class DeleteViewStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = models.Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:index')
    success_message = 'Status deleted'
    login_url = reverse_lazy('statuses:delete')
    
    def post(self, request, *args, **kwargs):
        try:
            response = self.delete(request, *args, **kwargs)
            messages.success(request, 'Status deleted') 
            return response
        except ProtectedError:
            messages.error(request, 'Статус не может быть удален, так как он используется')
            return redirect(reverse_lazy('statuses:index'))