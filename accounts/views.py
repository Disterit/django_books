from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationFrom


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'