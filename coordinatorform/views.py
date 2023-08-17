from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import LoginPage, RegisterPage
from django.contrib.auth import login, authenticate
from .models import Coordinator
from django.views.generic import ListView, DetailView
# Create your views here.
def homeView(request):
    return render(request, 'coordinatorform/welcome.html') #templates\coordinatorform

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
    # sourcery skip: extract-method, remove-unnecessary-else
    error = None
    err = False
    if(request.method == 'POST'):
        form = RegisterPage(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            err = True
            error = 'Please fix the errors.'
    else:
        form = RegisterPage()
    return render(request, 'coordinatorform/register.html', context={'form':form, 'error':error, 'err':err})
def ProfileView(request):
    userData = request.user
    user = {
        "fullname": userData.fullname,
        "nickname": userData.nickname,
        "dateofbirth": userData.dateofbirth,
        "religion": userData.religion,
        "school": userData.school,
        "college": userData.college,
        "email": userData.email,
        "contact": userData.contact,
        "praddress": userData.praddress,
        "peraddress": userData.peraddress,
        "district": userData.district,
        "facebook": userData.facebook
        if userData.facebook.find("https://") != -1
        else f"https://{userData.facebook}",
        "instagram": userData.instagram
        if userData.instagram.find('https://') != -1
        else f"https://{userData.instagram}",
        "twitter": userData.twitter
        if userData.twitter.find('https://') != -1
        else f"https://{userData.twitter}",
        "whatsapp": userData.whatsapp
        if userData.whatsapp.find('https://') != -1
        else f"https://{userData.whatsapp}",
        "linkedin": userData.linkedin
        if userData.linkedin.find('https://') != -1
        else f"https://{userData.linkedin}",
        "picture": userData.picture,
        "experience": sorted(list(userData.experience.split("\r\n")))
        if userData.experience != None
        else userData.experience,
        "skills": sorted(list(userData.skills.split("\r\n")))
        if userData.skills != None
        else userData.skills,
        "interests": sorted(list(userData.interests.split("\r\n")))
        if userData.interests != None
        else userData.interests,
        "username": userData.username,
    }
    return render(request, 'coordinatorform/profile.html', context={'data':user})

class CoordinatorListView(ListView):
    model = Coordinator
    context_object_name = 'coordinator_list'
class CoordinatorDetailView(DetailView):
    model = Coordinator
    