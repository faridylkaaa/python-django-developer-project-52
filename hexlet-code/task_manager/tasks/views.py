from django.shortcuts import render
from django.views import View
from task_manager.tasks import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages
from task_manager import mixins
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import CreateTaskForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.mixins import AuthorAccessMixin


# Create your views here.
class IndexView(LoginRequiredMixin, View):
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/index.html', {'tasks': tasks})
    
class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateTaskForm
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:index')
    login_url = reverse_lazy('users:login')
    success_message = 'Задание создано'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = forms.UpdateTaskForm
    permission_denied_message = 'Необходимо войти или зарегестрироваться'
    template_name = 'tasks/update.html'
    success_message = 'Форма изменена'
    success_url = reverse_lazy('tasks:index')
    login_url = reverse_lazy('users:login')
    
class TaskDeleteView(AuthorAccessMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_message = 'Задача удалена'
    template_name = 'tasks/delete.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('tasks:index')
    
class TaskView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        task = Task.objects.get(id=pk)
        if task:
            return render(request, 'tasks/show.html', {'task': task})
        else:
            messages.error(request, 'Задачи не существует')
            return redirect(reverse_lazy('tasks:index'))