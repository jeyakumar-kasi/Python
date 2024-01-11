# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:59:13 2023

@author: Jeyak
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# User Creation
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username"
        )
        
        
# User Change
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username"
        )