from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import Coordinator
class LoginPage(forms.Form):
    username = forms.CharField(label='Username', max_length=63, widget=forms.TextInput(
        attrs= {
            "id" : "username",
            "name" : "username",
            "autofocus" : True,
            "placeholder" : "Enter your username"            
        }
    ))
    password = forms.CharField(label="Password", max_length=63, widget=forms.PasswordInput(
        attrs= {
            "id": "password",
            "name": "password",
            "placeholder" : "Enter your password"
        }
    ))



class RegisterPage(UserCreationForm):
    class Meta:
        model = Coordinator
        fields = ("fullname", "nickname", "dateofbirth", "religion", "school", "college", "email", "contact", "praddress", "peraddress", "district", "facebook", "picture", "experience", "skills", "interests", "username")
        labels = {
            'fullname': 'Full Name',
            "nickname": "Nickname",
            "dateofbirth": "Date of Birth",
            "religion": "Religion",
            "school": "School",
            "college": "College",
            "email": "Email Address",
            "contact": "Contact Number",
            "praddress": "Present Address",
            "peraddress": "Permanent Address",
            "district": "District",
            "facebook": "Facebook Profile",
            "picture": "Upload your profile picture [300px X 300px]",
            "experience": "Experiences [Separate them with semicolons]",
            "skills": "Skills [Separate them with semicolons]",
            "interests": "Interests [Separate them with semicolons]",
            "username": "Username",
        }
        widgets = {
            'fullname': widgets.TextInput(attrs={'placeholder':'Your Full name', 'autofocus':True}),
            'nickname': widgets.TextInput(attrs={'placeholder':'Your Nickname'}),
            'dateofbirth' : widgets.DateInput(attrs={'type':'date'}),
            'email' : widgets.EmailInput(attrs={'type':'email', 'placeholder':'example@gmail.com'}),
            'school': widgets.TextInput(attrs={'placeholder':'Your College'}),
            'college': widgets.TextInput(attrs={'placeholder':'Your School'}),
            'contact': widgets.TextInput(attrs={'placeholder':'+8801345678910'}),
            'religion': widgets.TextInput(attrs={'placeholder':'Islam/Hinduism/Christianity/Buddhism'}),
            'district': widgets.TextInput(attrs={'placeholder':'Your District'}),
            'facebook': widgets.TextInput(attrs={'placeholder':'Your facebook profile link'}),
            'praddress': widgets.TextInput(attrs={'placeholder':'House, Road, Thana, Area, Upazila'}),
            'peraddress': widgets.TextInput(attrs={'placeholder':'House, Road, Thana, Area, Upazila'}),
            'experience': widgets.TextInput(attrs={'placeholder':'Organizations you previously worked or currently working'}),
            'skills': widgets.TextInput(attrs={'placeholder':'Your Skills'}),
            'interests': widgets.TextInput(attrs={'placeholder':'Your Interests'}),
            'username': widgets.TextInput(attrs={'placeholder':'Enter a username'}),
        }
    



















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