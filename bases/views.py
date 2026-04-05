from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

##LoginRequiredMixin aqui exige que el usuario este autenticado para ver la vista
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    ###Si el usuario no esta logeado nos redireccionara a:
    login_url='bases:login'