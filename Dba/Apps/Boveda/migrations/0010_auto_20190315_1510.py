# Generated by Django 2.1.7 on 2019-03-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boveda', '0009_auto_20190315_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicio',
            name='Tipo',
            field=models.CharField(choices=[('F', 'Fisico'), ('O', 'Organico'), ('B', 'Biologico'), ('FO', 'Fisico/Organico')], default='F', max_length=2),
        ),
    ]
