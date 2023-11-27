# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:49:02 2023

@author: r_daitou
"""

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):#371
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')