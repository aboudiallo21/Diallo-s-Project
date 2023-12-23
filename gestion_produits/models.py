from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    DEFAULT_CODE = 'DEFAULT_CODE'
    DEFAULT_NAME = 'DEFAULT_NAME'
    DEFAULT_DESCRIPTION = 'DEFAULT_DESCRIPTION'

    code_name = models.CharField(max_length=100, default=DEFAULT_CODE)
    name = models.CharField(max_length=100, default=DEFAULT_NAME)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

class Panier(models.Model):
    DEFAULT_CODE_PANIER = 'DEFAULT_CODE_PANIER'
    DEFAULT_LABEL = 'DEFAULT_LABEL'
    DEFAULT_DESCRIPTION = 'DEFAULT_DESCRIPTION'

    code_panier = models.CharField(max_length=100, default=DEFAULT_CODE_PANIER)
    label = models.CharField(max_length=100, default=DEFAULT_LABEL)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    products = models.ManyToManyField(Product, through='Ponderation')

class Ponderation(models.Model):
    DEFAULT_PONDERATION = 0.0

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField(default=DEFAULT_PONDERATION)




class pointvente(models.Model):
    DEFAULT_ZONE = 'DEFAULT_ZONE'
    DEFAULT_GPS = 'DEFAULT_GPS'

    zone = models.CharField(max_length=100, default=DEFAULT_ZONE)
    gps = models.CharField(max_length=100, default=DEFAULT_GPS)

class Price(models.Model):
    DEFAULT_VALUE = 0.0

    value = models.FloatField(default=DEFAULT_VALUE)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    zone = models.ForeignKey(pointvente, on_delete=models.CASCADE)