from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from coordinatorform.models import Coordinator
from coordinatorform.forms import RegisterPage
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Coordinator
    add_form = RegisterPage
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'fullname',
                    'nickname',
                    'dateofbirth',
                    'religion',
                    'school',
                    'college',
                    'contact',
                    'praddress',
                    'peraddress',
                    'facebook',
                    'instagram',
                    'twitter',
                    'whatsapp',
                    'linkedin',
                    'picture',
                    'district',
                    'experience',
                    'skills',
                    'interests',
                )
            }
        )
    )
    list_display = ["username", "image_tag", "email", "nickname", "is_staff"]
admin.site.register(Coordinator, CustomUserAdmin)