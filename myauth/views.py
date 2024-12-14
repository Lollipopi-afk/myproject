from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class AboutMeView(TemplateView):
    template_name = 'myauth/about-me.html'

class RegisterView(CreateView): #регистрация пользователя
    form_class = UserCreationForm 
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me') 
    def form_valid(self, form):
        print(form.cleaned_data)  
        response = super().form_valid(form) 

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        print(f'Username: {username}, Password: {password}') 

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            print(f'User authenticated: {user.username}') 
            login(self.request, user)
        else:
            print('Authentication failed')  

        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)  
            return redirect('/admin/')  
        else:
            return render(request, 'myauth/login.html', {'form': form, 'error': 'Неверные данные для входа'})  
    
    form = AuthenticationForm()
    return render(request, 'myauth/login.html', {'form': form})


def logout_view(request: HttpRequest): 
    logout(request)
    return redirect(reverse('myauth:login')) 



