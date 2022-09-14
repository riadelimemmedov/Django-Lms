from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserForm
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Gives Roles User',
            {
                'fields':(
                    'role',
                )
            }
        )
    )
admin.site.register(CustomUser,CustomUserAdmin)