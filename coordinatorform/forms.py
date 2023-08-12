from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import coOrdinator
class LoginPage(forms.Form):
    username = forms.CharField(label='Username', max_length=63, widget=forms.TextInput(
        attrs= {
            "id" : "username",
            "name" : "username",
        }
    ))
    password = forms.CharField(label="Password", max_length=63, widget=forms.PasswordInput(
        attrs= {
            "id": "password",
            "name": "password",
        }
    ))



class RegisterPage(UserCreationForm):
    class Meta:
        model = coOrdinator
        fields = ("fullname", "nickname", "dateofbirth", "religion", "school", "college", "email", "contact", "address", "upazila", "district", "picture", "exp", "username")
        labels = {
            'fullname': 'Full Name',
            "nickname": "Nickname",
            "dateofbirth": "Date of Birth",
            "religion": "Religion",
            "school": "School",
            "college": "College",
            "email": "Email Address",
            "contact": "Contact Number",
            "address": "Address",
            "upazila": "Upazila",
            "district": "District",
            "picture": "Upload your profile picture (300px X 300px)",
            "exp": "Experience",
            "username": "Username",
        }
    def clean(self):  # sourcery skip: inline-immediately-returned-variable
        cleaned = self.cleaned_data
        data = cleaned.get("username")
        print(data)



















        # fullname = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "fullname",
    #         "name" : "fullname",
    #     }
    # ))
    # nickname = forms.CharField(label="Nickname", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "nickname",
    #         "name" : "nickname",
    #     }
    # ))
    # dateofbirth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
    #     attrs= {
    #         "id" : "dateofbirth",
    #         "name" : "dateofbirth",
    #     }
    # ))
    # religion = forms.CharField(label="Religion", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "religion",
    #         "name" : "religion",
    #     }
    # ))
    # school = forms.CharField(label="School", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "school",
    #         "name" : "school",
    #     }
    # ))
    # college = forms.CharField(label="College", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "college",
    #         "name" : "college",
    #     }
    # ))
    # email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(
    #     attrs= {
    #         "id" : "email",
    #         "name" : "email",
    #     }
    # ))
    # contact = forms.CharField(label="Contact Number", max_length=15, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "contact",
    #         "name" : "contact",
    #     }
    # ))
    # address = forms.CharField(label="Address", max_length=500, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "address",
    #         "name" : "address",
    #     }
    # ))
    # upazila = forms.CharField(label="Upazila", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "upazila",
    #         "name" : "upazila",
    #     }
    # ))
    # district = forms.CharField(label="District", max_length=50, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "district",
    #         "name" : "district",
    #     }
    # ))
    # picture = forms.FileField(label="Picture", max_length=100, widget=forms.FileInput(
    #     attrs= {
    #         "id" : "picture",
    #         "name" : "picture",
    #     }
    # ))
    # username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "username",
    #         "name" : "username",
    #     }
    # ))
    # password = forms.CharField(label="Password", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "password",
    #         "name" : "password",
    #     }
    # ))
    # cpassword = forms.CharField(label="Confirm Password", max_length=100, widget=forms.TextInput(
    #     attrs= {
    #         "id" : "cpassword",
    #         "name" : "cpassword",
    #     }
    # ))