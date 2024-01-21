#def calculate_price_index(prices):
 #   total_value = sum(price.value for price in prices)
#   num_prices = len(prices)
 #   if num_prices > 0:
#        price_index = total_value / num_prices
 #   else:
 #       price_index = 0
 #   return price_index

from functools import reduce


def calculate_price_index(prices):
    total_weighted = 0.0
    total_weight = 0.0

    for price in prices:
        value_as_float = float(price.value)

        # Vérifiez si price.ponderation est None
        if price.ponderation is not None:
            ponderation_as_float = float(price.ponderation.ponderation)

            weighted_price = value_as_float * ponderation_as_float
            total_weighted += weighted_price
            total_weight += ponderation_as_float

    if total_weight != 0:
        price_index = total_weighted / total_weight
        return price_index
    else:
        return None


from .models import Price, Ponderation, Panier

def calculate_price_index_by_panier():
    # Initialiser un dictionnaire pour stocker les totaux pondérés et les poids totaux pour chaque panier
    totals = {}

    # Parcourir tous les prix
    for price in Price.objects.all():
        # Vérifiez si price.ponderation est None
        if price.ponderation.ponderation is not None:
            ponderation_as_float = float(price.ponderation.ponderation)
            panier = price.ponderation.panier.code_panier

            # Initialiser les totaux pour ce panier si nécessaire
            if panier not in totals:
                totals[panier] = {'total_weighted': 0.0, 'total_weight': 0.0}

            weighted_price = float(price.value) * ponderation_as_float
            totals[panier]['total_weighted'] += weighted_price
            totals[panier]['total_weight'] += ponderation_as_float

    # Calculer l'indice de prix pour chaque panier
    price_indices = {}
    for panier, totals in totals.items():
        if totals['total_weight'] != 0:
            price_index = totals['total_weighted'] / totals['total_weight']
            price_indices[panier] = price_index

    return price_indices
