from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Champ de description facultatif

    def __str__(self):
        return self.name


class Product(models.Model):
    DEFAULT_CODE = 'DEFAULT_CODE'
    DEFAULT_NAME = 'DEFAULT_NAME'
    DEFAULT_DESCRIPTION = 'DEFAULT_DESCRIPTION'

    code_name = models.CharField(max_length=100, default=DEFAULT_CODE)
    name = models.CharField(max_length=100, default=DEFAULT_NAME)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Panier(models.Model):
    DEFAULT_CODE_PANIER = 'DEFAULT_CODE_PANIER'
    DEFAULT_LABEL = 'DEFAULT_LABEL'
    DEFAULT_DESCRIPTION = 'DEFAULT_DESCRIPTION'

    code_panier = models.CharField(max_length=100, default=DEFAULT_CODE_PANIER)
    label = models.CharField(max_length=100, default=DEFAULT_LABEL)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    products = models.ManyToManyField(Product, through='Ponderation')

    def __str__(self):
        return f"{self.code_panier} - {self.label}"


class Ponderation(models.Model):
    DEFAULT_PONDERATION = 0.0

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField(default=DEFAULT_PONDERATION)

    def __str__(self):
        return f"{self.ponderation} "




class pointvente(models.Model):
    DEFAULT_ZONE = 'DEFAULT_ZONE'
    DEFAULT_GPS = 'DEFAULT_GPS'
    DEFAULT_WILAYA = 'DEFAULT_WILAYA'
    DEFAULT_MOUGATAA = 'DEFAULT_MOUGATAA    '
    zone = models.CharField(max_length=100, default=DEFAULT_ZONE)
    gps = models.CharField(max_length=100, default=DEFAULT_GPS)
    wilaya = models.CharField(max_length=100,default=DEFAULT_WILAYA)  # Champ pour la wilaya
    mougataa = models.CharField(max_length=100,default=DEFAULT_MOUGATAA )

    def __str__(self):
        return f"{self.zone} "

class Price(models.Model):
    DEFAULT_VALUE = 0.0
    value = models.FloatField(default=DEFAULT_VALUE)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    zone = models.ForeignKey(pointvente, on_delete=models.CASCADE)
    ponderation = models.OneToOneField(Ponderation, on_delete=models.CASCADE, null=True, blank=True)