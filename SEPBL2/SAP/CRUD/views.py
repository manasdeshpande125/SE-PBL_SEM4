from dataclasses import field, fields
from pyexpat import model
from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from requests import request
from .models import Achievements,profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import login
from .forms import   UpdateUserForm,UserForm,EditProfileForm
from django.contrib.auth.views import PasswordResetView

# Create your views here.
def group(request):
    return render(request, 'CRUD/group.html')

class SAP(LoginRequiredMixin,ListView):
    model=Achievements
    context_object_name='SAP'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['SAP'] = context['SAP'].filter(user=self.request.user)
        #context['count']=context['SAP'].filter(description=False).count()

        '''search_input=self.request.GET.get('search_area') or ''
        if search_input:
            context['SAP'] = context['SAP'].filter(title__startswith=search_input)
        context['search_input'] = search_input'''
        return context


#<!--{%for Achievements in object_list %}-->//for all details
class admin1(LoginRequiredMixin,ListView):
    model=Achievements
    context_object_name='SAP'
    template_name="CRUD/admin.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['SAP'] = context['SAP'].filter(user=self.request.user)
        search_input=self.request.GET.get('search_area') or ''
        if search_input is not None:
            context['SAP'] = context['SAP'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


class Details(LoginRequiredMixin,DetailView):
    model=Achievements
    context_object_name='Details'

class New(LoginRequiredMixin,CreateView):
    model=Achievements
    fields=['title', 'description','support','certificate']
    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.roll_no=request.user.roll_no
        return super().form_valid(form)
    success_url=reverse_lazy('SAP')

class Edit(LoginRequiredMixin,UpdateView):
    model=Achievements
    fields=['title', 'description','support','certificate']
    success_url=reverse_lazy('SAP')

class delete(LoginRequiredMixin,DeleteView):
    model=Achievements
    context_object_name='Delete'
    success_url=reverse_lazy('SAP')


class CustomLoginView(LoginView):
    template_name='CRUD/login.html'
    fields="__all__"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('SAP')

class RegisterPage(FormView,CreateView):
    template_name='CRUD/register.html'
    #form_class=UserCreationForm
    form_class=UserForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('SAP')
    

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)

        return super(RegisterPage,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('SAP')
        return super(RegisterPage,self).get(*args, *kwargs)




class UserEditView(LoginRequiredMixin,UpdateView):
    template_name="CRUD/update.html"
    form_class=EditProfileForm
    success_url=reverse_lazy('SAP')

    
    def get_object(self):
        return self.request.user
     



class New1(LoginRequiredMixin,CreateView):
    model=profile
    fields=['roll', 'div','year','dept']
    template_name="CRUD/new_profile.html"
    context_object_name='profiles'

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        #form.instance.roll_no=request.user.roll_no
        return super().form_valid(form)
    success_url=reverse_lazy('SAP')


class Edit1(LoginRequiredMixin,UpdateView):
    model=profile
    fields=['roll', 'div','year','dept']
    template_name="CRUD/edit_profile.html"
    success_url=reverse_lazy('SAP')




class prof(LoginRequiredMixin,ListView):
    model=profile
    context_object_name='prof'
    template_name="CRUD/profile_list.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['prof'] = context['prof'].filter(user=self.request.user)
        #context['count']=context['SAP'].filter(description=False).count()

        '''search_input=self.request.GET.get('search_area') or ''
        if search_input:
            context['SAP'] = context['SAP'].filter(title__startswith=search_input)
        context['search_input'] = search_input'''
        return context