# Generated by Django 2.0.6 on 2018-07-24 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_concesionrio_tipo_combustible'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tipo_combustible',
            new_name='Combustible',
        ),
    ]
