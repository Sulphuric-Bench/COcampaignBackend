from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import LoginPage, RegisterPage
from django.contrib.auth import login, authenticate
# Create your views here.
def homeView(request):
    return render(request, 'coordinatorform/welcome.html') #templates\coordinatorform

class ProfileView(DetailView):
    pass

def login_page(request):  # sourcery skip: remove-unreachable-code
    form = LoginPage()
    message = 'Login as Co-ordinator!'
    error = "CONTINUE"
    err = False
    if (request.method == 'POST'):
        form = LoginPage(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f"Hello {user.username.capitalize()}!"
                return redirect('Home')
            else:
                err = True
                error = 'Login Failed! Please Try Again.'
        else:
            err = True
            error = 'Login Failed! Please Try Again.'
    return render(request, 'registration/login.html', context={'form':form, 'message': message, 'err':err, 'error': error})
def register_page(request):
    error = None
    err = False
    if(request.method == 'POST'):
        form = RegisterPage(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            err = True
            error = 'Something was wrong! Please Try Again.'
    else:
        form = RegisterPage()
    return render(request, 'coordinatorform/register.html', context={'form':form, 'error':error, 'err':err})