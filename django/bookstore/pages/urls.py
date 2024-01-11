# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:30:26 2023

@author: Jeyak
"""

from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page")    
]