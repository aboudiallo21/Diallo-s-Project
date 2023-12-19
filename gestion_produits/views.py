# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Family, Product
from .forms import FamilyForm, ProductForm
from .utils import calculate_price_index


def family_list(request):
    families = Family.objects.all()
    return render(request, 'family_list.html', {'families': families})

def family_detail(request, pk):
    family = get_object_or_404(Family, pk=pk)
    return render(request, 'family_detail.html', {'family': family})

def family_new(request):
    if request.method == "POST":
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save(commit=False)
            family.save()
            return redirect('family_detail', pk=family.pk)
    else:
        form = FamilyForm()
    return render(request, 'family_edit.html', {'form': form})

def family_edit(request, pk):
    family = get_object_or_404(Family, pk=pk)
    if request.method == "POST":
        form = FamilyForm(request.POST, instance=family)
        if form.is_valid():
            family = form.save(commit=False)
            family.save()
            return redirect('family_detail', pk=family.pk)
    else:
        form = FamilyForm(instance=family)
    return render(request, 'family_edit.html', {'form': form})

def family_delete(request, pk):
    family = get_object_or_404(Family, pk=pk)
    family.delete()
    return redirect('family_list')

# Similar views for Product CRUD operations...
# views.py

# ... (imports)

# Views for Product CRUD operations

def product_list(request):
    products = Product.objects.all()
    prices = [product.price for product in products]  # Récupération des prix des produits
    price_index = calculate_price_index(prices)  # Calcul de l'indice de prix

    context = {
        'products': products,
        'price_index': price_index,
    }
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_new(request):
    print(request.method)
    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

