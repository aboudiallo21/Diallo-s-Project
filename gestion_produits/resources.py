from import_export import resources
from .models import Price
from import_export import resources, fields
#class PriceResource(resources.ModelResource):
#    product_name = fields.Field(attribute='product__name', column_name='product name')
#    zone_name = fields.Field(attribute='zone__zone', column_name='zone name')

#    class Meta:
#        model = Price
#        fields = ('value', 'date', 'product_name', 'zone_name', 'ponderation')
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Price, Product, pointvente

class PriceResource(resources.ModelResource):
    product = fields.Field(
        column_name='product name',
        attribute='product',
        widget=ForeignKeyWidget(Product, 'name'))
    zone = fields.Field(
        column_name='zone name',
        attribute='zone',
        widget=ForeignKeyWidget(pointvente, 'zone'))

    class Meta:
        model = Price
        import_id_fields = ['product', 'zone', 'value', 'date', 'ponderation']
        fields = ('product', 'zone', 'value', 'date', 'ponderation')