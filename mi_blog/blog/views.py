from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, UpdateView, TemplateView
from .models import Page, Profile
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

from django.contrib import messages

from django.contrib.auth.models import User


from django.views import generic

class PageListView(ListView):
    model = Page
    template_name = 'templates/blog/page_list.html'  # Nombre del template que crearemos
    context_object_name = 'pages'  # Nombre del objeto en la plantilla

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'



class InicioView(TemplateView):
    template_name = 'blog/inicio.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mostrar_titulos'] = True
        return context

# Crear página
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'summary', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('page-list')


# Editar página
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'summary', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('page-list')


# Borrar página
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('page-list')


class ContactoView(TemplateView):
    template_name = 'blog/contacto.html'

class AcercaDeView(TemplateView):
    template_name = 'blog/acerca.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'blog/profile.html'

    def get_object(self,queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio', 'avatar']
    template_name = 'blog/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "¡Te has registrado exitosamente! Ahora puedes iniciar sesión.")
        return response

    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'email','password1', 'password2']