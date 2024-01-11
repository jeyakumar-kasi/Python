from django.contrib import admin

from django.contrib.auth import get_user_model
CustomUser = get_user_model()


from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = [
        "email",
        "username",
        #"password",
        #"user_permissions",
        #"groups",
        "last_login",
        "date_joined",
        "is_superuser",
        "is_staff",
        "is_active",
    ]

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
