from django.shortcuts import render, get_object_or_404, redirect
from .models import Family, Product, Panier, Ponderation, Price, pointvente
from .forms import *  # Assurez-vous d'avoir les formulaires appropriés pour Family et Product


def family_list(request):
    families = Family.objects.all()
    return render(request, 'family_list.html', {'families': families})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def family_detail(request, pk):
    family = get_object_or_404(Family, pk=pk)
    return render(request, 'family_detail.html', {'family': family})

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

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

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


# ...importations et vues précédentes...

def panier_list(request):
    paniers = Panier.objects.all()
    return render(request, 'panier_list.html', {'paniers': paniers})

# Ajoutez des vues pour panier_detail, panier_edit, panier_new, panier_delete, etc., de manière similaire...

def price_list(request):
    prices = Price.objects.all()
    price_form = PriceForm()  # Initialize an empty form
    return render(request, 'price_list.html', {'prices': prices, 'price_form': price_form})
# Ajoutez des vues pour price_detail, price_edit, price_new, price_delete, etc., de manière similaire...

def ponderation_list(request):
    ponderations = Ponderation.objects.all()
    return render(request, 'ponderation_list.html', {'ponderations': ponderations})

# Ajoutez des vues pour ponderation_detail, ponderation_edit, ponderation_new, ponderation_delete, etc., de manière similaire...



# Ajoutez des vues pour point_de_vente_detail, point_de_vente_edit, point_de_vente_new, point_de_vente_delete, etc., de manière similaire...
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

def family_delete(request, pk):
    family = get_object_or_404(Family, pk=pk)
    family.delete()
    return redirect('family_list')

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


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')





def price_add(request):
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('price_list')  # Rediriger vers la liste des prix après l'ajout
    else:
        form = PriceForm()

    return render(request, 'price_add.html', {'form': form})


def price_detail(request, pk):
    price = get_object_or_404(Price, pk=pk)
    return render(request, 'price_detail.html', {'price': price})

def price_edit(request, pk):
    price = get_object_or_404(Price, pk=pk)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            price = form.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm(instance=price)
    return render(request, 'price_edit.html', {'form': form})




def panier_list(request):
    paniers = Panier.objects.all()
    return render(request, 'panier_list.html', {'paniers': paniers})

def panier_detail(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    return render(request, 'panier_detail.html', {'panier': panier})

def panier_edit(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    if request.method == "POST":
        form = PanierForm(request.POST, instance=panier)
        if form.is_valid():
            panier = form.save()
            return redirect('panier_detail', pk=panier.pk)
    else:
        form = PanierForm(instance=panier)
    return render(request, 'panier_edit.html', {'form': form})

def panier_add(request):
    if request.method == "POST":
        form = PanierForm(request.POST)
        if form.is_valid():
            panier = form.save()
            return redirect('panier_detail', pk=panier.pk)
    else:
        form = PanierForm()
    return render(request, 'panier_add.html', {'form': form})

def ponderation_edit(request, pk):
    ponderation = get_object_or_404(Ponderation, pk=pk)
    if request.method == "POST":
        form = PonderationForm(request.POST, instance=ponderation)
        if form.is_valid():
            ponderation = form.save(commit=False)
            ponderation.save()
            return redirect('ponderation_list')
    else:
        form = PonderationForm(instance=ponderation)
    return render(request, 'ponderation_edit.html', {'form': form})

def ponderation_add(request):
    if request.method == "POST":
        form = PonderationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('ponderation_list')
    else:
        form = PonderationForm()
    return render(request, 'ponderation_add.html', {'form': form})

def ponderation_detail(request, pk):
    ponderation = get_object_or_404(Ponderation, pk=pk)
    return render(request, 'ponderation_detail.html', {'ponderation': ponderation})

def ponderation_delete(request, pk):
    ponderation = get_object_or_404(Ponderation, pk=pk)
    if request.method == 'POST':
        ponderation.delete()
        return redirect('ponderation_list')  # Redirige où vous voulez après la suppression
    return render(request, 'ponderation_delete.html', {'ponderation': ponderation})

def pointvente_list(request):
    points_de_vente = pointvente.objects.all()
    return render(request, 'pointvente_list.html', {'points_de_vente': points_de_vente})


def panier_delete(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    if request.method == 'POST':
        panier.delete()
        return redirect('nom_de_la_vue_liste_des_paniers')  # Remplacez 'nom_de_la_vue_liste_des_paniers' par le nom de la vue pour la liste des paniers
    return render(request, 'panier_delete.html', {'panier': panier})



from .utils import calculate_price_index

def price_list(request):
    prices = Price.objects.all()
    price_index = calculate_price_index(prices)

    return render(
        request,
        'price_list.html',
        {
            'prices': prices,
            'price_index': price_index,
        }
    )


def pointvente_add(request):
    if request.method == 'POST':
        pointvente_form = pointventeForm(request.POST)
        if pointvente_form.is_valid():
            pointvente_form.save()
            # Redirection ou traitement après l'ajout
    else:
        pointvente_form = pointventeForm()

    return render(request, 'pointvente_add.html', {'pointvente_form': pointvente_form})