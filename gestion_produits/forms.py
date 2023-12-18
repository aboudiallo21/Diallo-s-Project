# forms.py

from django import forms
from .models import Family, Product

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name', 'description')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'family')
