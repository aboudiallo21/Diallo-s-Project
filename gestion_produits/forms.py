from django import forms
from .models import Family, Product, Panier, Ponderation, Price, pointvente

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name','description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('code_name', 'name', 'description', 'family')
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Modifier le champ 'family' pour afficher le nom de la famille
        self.fields['family'].label_from_instance = lambda obj: f'{obj.name}'
class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['code_panier', 'label', 'description', 'products']

class PonderationForm(forms.ModelForm):
    class Meta:
        model = Ponderation
        fields = ['product', 'panier', 'ponderation']




class pointventeForm(forms.ModelForm):
    class Meta:
        model = pointvente
        fields = ['zone', 'gps','wilaya','mougataa']
class PriceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PriceForm, self).__init__(*args, **kwargs)
        # Modifier le champ 'product' pour afficher le nom du produit
        self.fields['product'].label_from_instance = lambda obj: f'{obj.code_name} - {obj.name}'

    class Meta:
        model = Price
        fields = ['value', 'date', 'product','zone','ponderation']