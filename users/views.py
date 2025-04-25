from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser
from .forms import UserRegistrationForm

class UserRegistrationView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('book-list')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have been logged out.')
        return super().dispatch(request, *args, **kwargs) 