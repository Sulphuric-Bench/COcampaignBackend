from django.urls import path
from .views import homeView, ProfileView, login_page, register_page

urlpatterns = [
    path('', homeView, name='Home'),
    path('accounts/register/', register_page , name='register'),
    path('accounts/profile/', ProfileView , name='profile'),
    path('accounts/login/', login_page, name='login')
]