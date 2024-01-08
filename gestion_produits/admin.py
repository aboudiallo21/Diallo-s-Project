from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Family)
admin.site.register(models.Product)
admin.site.register(models.Panier)
admin.site.register(models.Ponderation)
admin.site.register(models.Price)
admin.site.register(models.pointvente)

