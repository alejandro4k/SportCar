# Generated by Django 2.0.6 on 2018-08-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_marca_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='foto',
            field=models.ImageField(blank=True, default='defaul.jpg', null=True, upload_to='autos'),
        ),
    ]
