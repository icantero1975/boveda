# Generated by Django 2.1.7 on 2019-03-15 21:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Boveda', '0008_auto_20190315_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicio',
            name='Entrega',
        ),
        migrations.RemoveField(
            model_name='indicio',
            name='Fecha_Ingreso',
        ),
        migrations.RemoveField(
            model_name='indicio',
            name='Hora_Ingreso',
        ),
        migrations.RemoveField(
            model_name='indicio',
            name='Oficio',
        ),
        migrations.AddField(
            model_name='expediente',
            name='Fecha_Ingreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expediente',
            name='Hora_Ingreso',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expediente',
            name='Oficio',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediente',
            name='Titular',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Boveda.Mp'),
        ),
        migrations.AddField(
            model_name='indicio',
            name='Persona_Entrega',
            field=models.CharField(default=django.utils.timezone.now, help_text='Ingrese Nombre de quien entrega fisicamente el indicio', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indicio',
            name='Clasificacion',
            field=models.CharField(choices=[('AC', 'Arma de Fuego Corta'), ('AL', 'Arma de Fuego Larga'), ('AB', 'Arma Blanca'), ('EM', 'Estupefaciente-Marihuana'), ('EC', 'Estupefaciente-Cocaina'), ('EH', 'Estupefaciente-Heroina'), ('EA', 'Estupefaciente-Anfetamina'), ('EL', 'Estupefaciente-Cristal'), ('T', 'Tabaco'), ('AL', 'Alcohol'), ('P', 'Perecedero'), ('E', 'Electronico'), ('AP', 'Autopartes'), ('H', 'Herramientas'), ('AB', ' Articulos de Belleza'), ('J', 'Joyeria'), ('R', ' Ropa'), ('N', ' Numerario'), ('O', 'Otro')], default='A', max_length=2),
        ),
    ]
