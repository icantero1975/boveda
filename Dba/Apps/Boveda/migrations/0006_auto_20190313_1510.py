# Generated by Django 2.1.7 on 2019-03-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boveda', '0005_auto_20190313_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicio',
            name='Peso_Narcotico',
            field=models.FloatField(default=0.0),
        ),
    ]
