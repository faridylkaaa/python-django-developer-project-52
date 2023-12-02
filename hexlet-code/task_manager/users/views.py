from django.shortcuts import render
from django.views import View
from task_manager.users import forms
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages
from task_manager import mixins
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', {'users': users})
    
    
class CreateUser(SuccessMessageMixin, CreateView):
    form_class = forms.CreateUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:login')
    login_url = reverse_lazy('users:login')
    success_message = 'User created'
    
class LoginUser(SuccessMessageMixin, LoginView):
    form_class = forms.LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main')
    success_message = 'User log in'
    login_url = reverse_lazy('users:login')
    
    def get_success_url(self):
        return self.success_url
    
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))

class UpdateUser(mixins.RightUserMixin, SuccessMessageMixin, UpdateView):
    form_class = forms.UpdateUserForm
    model = User
    # fields = ['username']
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:index')
    success_message = 'User updated'
    login_url = reverse_lazy('users:login')
            
class DeleteUser(mixins.RightUserMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('main')
    success_message = 'User deleted'
    login_url = reverse_lazy('users:login')
    
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Пользователь не может быть удален, так как у него есть задачи')
            return redirect(reverse('users:index'))