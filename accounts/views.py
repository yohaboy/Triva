from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegisterForm

class RegsiterUser(CreateView):
    model = CustomUser
    template_name = 'accounts/login-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request , user)

        return redirect(self.success_url)
    
class LoginUser(LoginView):
    template_name = 'accounts/login-register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')
