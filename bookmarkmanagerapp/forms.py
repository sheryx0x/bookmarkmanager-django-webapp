from django import forms
from .models import *



class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bookmark Title'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
        
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category Name'}),
        }