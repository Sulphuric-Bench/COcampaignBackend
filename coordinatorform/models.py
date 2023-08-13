from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.utils.safestring import mark_safe 
from PIL import Image as Im
# Create your models here.
class Coordinator(AbstractUser):
    fullname = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=50, blank=True)
    dateofbirth = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    praddress = models.CharField(max_length=1000, blank=True)
    peraddress = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to='profilepics/', blank=True, null=True, default='default.jpg')
    experience = models.CharField(max_length=10000, blank=True)
    skills = models.CharField(max_length=10000, blank=True)
    interests = models.CharField(max_length=10000, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True)
    
    is_reviewed = models.BooleanField(default=False)
    class Meta:
        permissions = (("is_reviewed", "new profile"),)
    def image_tag(self):   # sourcery skip: replace-interpolation-with-fstring
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.picture))
    def save(self, *args, **kwargs): # new
        super().save()
        img = Im.open(self.picture.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)