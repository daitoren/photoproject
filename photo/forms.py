# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:45:03 2023

@author: r_daitou
"""

from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']