# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:25:08 2023

@author: r_daitou
"""

from django.urls import path
from . import views

app_name = 'photo2'

urlpatterns = [
    path('photo/', views.PhotoView.as_view(), name='photo'),
    ]