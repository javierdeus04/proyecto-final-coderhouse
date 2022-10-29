from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



#class UsuarioLogin(LoginView):
    #template_name = 'usuarios/usuarios_login.html'
    #next_page = reverse_lazy("index")

#class UsuarioLogout(LogoutView):
    #template_name = 'blog/blog_logout.html'