from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.
class coOrdinator(AbstractUser):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    upazila = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    picture = models.FileField(blank=True, null=True, upload_to='files/')
    exp = models.CharField(max_length=10000, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    cpassword = models.CharField(max_length=100, blank=True, null=True)
