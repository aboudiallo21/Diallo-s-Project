# Generated by Django 5.0 on 2024-01-11 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_produits', '0009_pointvente_mougataa_pointvente_wilaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='ponderation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_produits.ponderation'),
        ),
    ]