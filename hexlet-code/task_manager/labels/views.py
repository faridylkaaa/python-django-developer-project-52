from django.shortcuts import render
from django.views import View
from task_manager.labels.models import Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.labels.forms import *
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
class IndexLabelView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/index.html', {'labels': labels})
    
class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateFormLabel
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels:index')
    login_url = reverse_lazy('users:login')
    success_message = 'Метка создана'
    
class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = CreateFormLabel
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    success_url = reverse_lazy('labels:index')
    success_message = 'Метка успешно изменена'
    login_url = reverse_lazy('users:login')
    template_name = 'labels/update.html'
    
class DeleteLabelView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')
    login_url = reverse_lazy('users:login')
    
    def post(self, request, *args, **kwargs):
        try:
            response = self.delete(request, *args, **kwargs)
            messages.success(request, 'Метка удалена')
            return response
        except ProtectedError:
            messages.error(request, 'Метка привязана')
            return redirect(reverse_lazy('labels:index'))