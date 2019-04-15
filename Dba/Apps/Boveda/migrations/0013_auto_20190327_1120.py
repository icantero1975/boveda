# Generated by Django 2.1.7 on 2019-03-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boveda', '0012_auto_20190319_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicio',
            name='Clasificacion',
            field=models.CharField(choices=[('AC', 'Arma de Fuego Corta'), ('AL', 'Arma de Fuego Larga'), ('AB', 'Arma Blanca'), ('EM', 'Estupefaciente-Marihuana'), ('EC', 'Estupefaciente-Cocaina'), ('EH', 'Estupefaciente-Heroina'), ('EA', 'Estupefaciente-Anfetamina'), ('EL', 'Estupefaciente-Cristal'), ('T', 'Tabaco'), ('AL', 'Alcohol'), ('P', 'Perecedero'), ('E', 'Electronico'), ('AP', 'Autopartes'), ('H', 'Herramientas'), ('AR', ' Articulos de Belleza'), ('J', 'Joyeria'), ('R', ' Ropa'), ('N', ' Numerario'), ('O', 'Otro')], default='A', max_length=2),
        ),
        migrations.AlterField(
            model_name='indicio',
            name='Dictamen',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='S', max_length=1),
        ),
    ]
