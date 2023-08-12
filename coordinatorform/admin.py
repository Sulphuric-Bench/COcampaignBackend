from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from coordinatorform.models import coOrdinator
from coordinatorform.forms import RegisterPage
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = coOrdinator
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
                    'address',
                    'upazila',
                    'district',
                    'exp',
                )
            }
        )
    )


admin.site.register(coOrdinator, CustomUserAdmin)