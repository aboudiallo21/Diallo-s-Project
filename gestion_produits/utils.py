def calculate_price_index(prices):
    if not prices:
        return None

    # Calcul de l'indice des prix à la consommation (IPC) simple
    index = sum(prices) / len(prices)  # Moyenne des prix

    return index
