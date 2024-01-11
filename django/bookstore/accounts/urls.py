# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:44:30 2023

@author: Jeyak
"""

from django.urls import path

from .views import SignupPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup')
]