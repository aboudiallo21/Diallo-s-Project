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

def pointvente_delete(request, pk):
    pointvente = get_object_or_404(pointvente, pk=pk)
    if request.method == 'POST':
        pointvente.delete()
        return redirect('pointvente_list')
    return render(request, 'pointvente_delete.html', {'pointvente': pointvente})



def pointvente_edit(request, pk):
    pointvente = get_object_or_404(pointvente, pk=pk)
    if request.method == "POST":
        form = pointventeForm(request.POST, instance=pointvente)
        if form.is_valid():
            pointvente = form.save(commit=False)
            pointvente.save()
            return redirect('pointvente_list')
    else:
        form = pointventeForm(instance=pointvente)
    return render(request, 'pointvente_edit.html', {'form': form})

def dashboard(request):
    # Récupérer les données des prix et des noms de produits
    prices = Price.objects.all()

    # Créer des listes pour les noms des produits et leurs prix associés
    produits = [price.product.name for price in prices]
    prix = [price.value for price in prices]

    # Passer les données récupérées au contexte du template
    context = {
        'produits': produits,
        'prix': prix,
    }

    return render(request, 'dashboard.html', context)


def house(request):
    return render(request, 'index.html')


def product_count(request):
    data = {
        "labels": [],
        "data": [],
    }
    for family in Family.objects.all():
        data["labels"].append(family.name)
        data["data"].append(Product.objects.filter(family=family).count())
    return JsonResponse(data)


from .resources import PriceResource
from django.http import HttpResponse
from .resources import PriceResource

#def export_data(request):
#    price_resource = PriceResource()
#    dataset = price_resource.export()
#    response = HttpResponse(dataset.csv, content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="prices.csv"'
#    return response

def export_data(request):
    price_resource = PriceResource()
    dataset = price_resource.export()
    with open('aboudiallo.csv', 'w') as f:
        f.write(dataset.csv)
    return HttpResponse("Les données ont été exportées avec succès dans le fichier 'aboudiallo.csv' du répertoire racine du projet.")

from django.contrib import messages
from tablib import Dataset
def import_data(request):
    if request.method == 'POST':
        price_resource = PriceResource()
        dataset = Dataset()
        new_prices = request.FILES['myfile']

        imported_data = dataset.load(new_prices.read().decode('utf-8'), format='csv')
        result = price_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            price_resource.import_data(dataset, dry_run=False)  # Actually import now
            # Afficher les lignes et les colonnes du fichier importé
            for ligne in imported_data:
                print(ligne)

            messages.success(request, 'Prices imported successfully')
            # Stocker les données importées dans la session de l'utilisateur
            request.session['imported_data'] = list(imported_data)
        else:
            messages.error(request, 'An error occurred during import')

    # Récupérer les données importées de la session de l'utilisateur
    imported_data = request.session.get('imported_data', [])

    return render(request, 'prices_list.html', {'imported_data': imported_data})


import csv
#from django.http import HttpResponse
#from .models import Price

#from django.shortcuts import render

#from django.contrib import messages
#from tablib import Dataset
#from .resources import PriceResource

#def import_prices(request):
#    if request.method == 'POST':
#        price_resource = PriceResource()
#        dataset = Dataset()
#        new_prices = request.FILES['myfile']

#        imported_data = dataset.load(new_prices.read().decode('utf-8'), format='csv')
#        result = price_resource.import_data(dataset, dry_run=True)  # Test the data import

 #       if not result.has_errors():
 #           price_resource.import_data(dataset, dry_run=False)  # Actually import now

#            messages.success(request, 'Prices imported successfully')
#        else:
#            messages.error(request, 'An error occurred during import')

#    return render(request, 'import.html', {'imported_data': imported_data})


from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import Price

#class LineChartJSONView(BaseLineChartView):
##    def get_labels(self):
#        """Return labels for the x-axis."""
        # Récupérer toutes les dates uniques des prix dans l'ordre
#        dates = Price.objects.dates('date', 'day').order_by('date')
#        labels = [date for date in dates]
#        return labels

#    def get_providers(self):
#        """Return all unique products."""
#        products = Price.objects.order_by('product').values('product').distinct()
#        return [price['product'] for price in products]

#    def get_data(self):
#        """Return datasets to plot."""
        # Récupérer tous les produits uniques
#        products = self.get_providers()
        # Créer une liste pour stocker les datasets
#        datasets = []
        # Pour chaque produit, créer un dataset
#        for product in products:
#            prices = Price.objects.filter(product__name=product).order_by('date')
#            data = [price.value for price in prices]
#            datasets.append(data)
 #       return datasets

#    def get_datasets(self, **kwargs):
#        """Return datasets for the plot."""
#        labels = self.get_labels()
#        data = self.get_data()
#        # Assurez-vous que les labels et les données sont de la même longueur
#        assert len(labels) == len(data)
#        # Créer les datasets
#        datasets = []
#        for i, product in enumerate(self.get_providers()):
#            datasets.append({
#                'label': product,
#                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
#                'borderColor': 'rgba(75, 192, 192, 1)',
#                'data': data[i],
#                'fill': False,
#            })
#        return datasets

#class LineChartView(TemplateView):
#    template_name = 'line_chart.html'

#line_chart = TemplateView.as_view(template_name='line_chart.html')
#line_chart_json = LineChartJSONView.as_view()

from django.shortcuts import render
from django.views.generic import TemplateView

class ChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['csv_file'] = "{% static 'aboudiallo.csv' %}"  # Remplacez par le chemin réel vers votre fichier CSV
        return context


# views.py
from django.http import JsonResponse
from django.db.models import Avg
from django.db.models.functions import ExtractYear

#def get_prices(request):
#    prices_by_year = Price.objects.annotate(year=ExtractYear('date')).values('year').annotate(avg_price=Avg('value')).order_by('year')
#    data = list(prices_by_year)  # convert QuerySet to list
#    return JsonResponse(data, safe=False)  # JsonResponse expects a dictionary -- use safe=False to allow list

def prices(request):
    return render(request, 'prices.html')

# views.py
from django.shortcuts import render
from django.db.models import Avg
from django.db.models.functions import ExtractYear

# views.py
# views.py
from django.shortcuts import render
from django.db.models import Avg
from django.db.models.functions import ExtractYear

# views.py
from django.shortcuts import render
from django.db.models import Avg
from django.db.models.functions import ExtractYear

def get_price_data():
    prices_by_year_and_product = Price.objects.annotate(year=ExtractYear('date')).values('year', 'product__name').annotate(avg_price=Avg('value')).order_by('product__name', 'year')
    data = list(prices_by_year_and_product)  # convert QuerySet to list
    return data

def prices(request):
    data = get_price_data()
    return render(request, 'prices.html', {'data': data})

def get_prices(request):
    data = get_price_data()
    return JsonResponse(data, safe=False)  # JsonResponse expects a dictionary -- use safe=False to allow list


from .models import Family
import io

def family_import(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Ce n\'est pas un fichier csv')
            return redirect('family_import')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Family.objects.update_or_create(
                name=column[0],
                description=column[1]
            )
        return redirect('family_list')
    else:
        return render(request, 'family_import.html')




def family_export(request):
    # Créer la réponse HTTP
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="families.csv"'

    # Créer un écrivain CSV
    writer = csv.writer(response)
    # Écrire l'en-tête du fichier CSV
    writer.writerow(['ID', 'Nom', 'Description'])

    # Récupérer toutes les familles
    families = Family.objects.all()

    # Écrire chaque famille dans le fichier CSV
    for family in families:
        writer.writerow([family.id, family.name, family.description])

    # Retourner la réponse
    return response


def product_import(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Ce n\'est pas un fichier csv')
            return redirect('product_import')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Product.objects.update_or_create(
                code_name=column[0],
                name=column[1],
                description=column[2],
                family=Family.objects.get(name=column[3])
            )
        return redirect('product_list')
    else:
        return render(request, 'product_import.html')


def product_export(request):
    # Créer la réponse HTTP
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    # Créer un écrivain CSV
    writer = csv.writer(response)
    # Écrire l'en-tête du fichier CSV
    writer.writerow(['Code', 'Nom', 'Description', 'Famille'])

    # Récupérer tous les produits
    products = Product.objects.all()

    # Écrire chaque produit dans le fichier CSV
    for product in products:
        writer.writerow([product.code_name, product.name, product.description, product.family.name])

    # Retourner la réponse
    return response
