from django.urls import reverse_lazy
from django.shortcuts import render,redirect

from django.views.generic import CreateView
from .forms import CustomUserCreationForm
class SignUpView(CreateView):
    form_class =CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='signup.html'
def history(request):
    return render(request,'history.html')