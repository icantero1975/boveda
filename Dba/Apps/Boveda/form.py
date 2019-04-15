from django import forms
from Dba.Apps.Boveda.models import *


class MpForm(forms.ModelForm):

    class Meta:
        model = Mp
        fields = [
            'Nombre',
            'Cargo',
            'Adscripcion',
        ]
        labels = {
            'Nombre':'Nombre del Responsable',
            'Cargo':'Cargo',
            'Adscripcion':'Adscripción',
        }
        widgets = {
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Cargo':forms.TextInput(attrs={'class':'form-control'}),
            'Adscripcion':forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExpedienteForm(forms.ModelForm):

    class Meta:
        model = Expediente
        fields = [
            'Cantidad_de_Indicios',
            'Resguardo_en',
            'Carpeta_Investigacion',
            'Titular',
            'Fecha_Ingreso',
            'Hora_Ingreso',
            'Oficio',

        ]
        labels ={
            'Cantidad_de_Indicios': '¿Cuantos Indicios Ingresan en esta Carpeta?',
            'Resguardo_en': 'Lugar de Resguardo de los Indicios',
            'Carpeta_Investigacion': 'Número de la Carpeta o Expediente de Investigación',
            'Titular':'Nombre de la Autoridad',
            'Fecha_Ingreso':'Fecha de Ingreso',
            'Hora_Ingreso':'Hora de Ingreso',
            'Oficio':'No. del Oficio',

        }


        widgets = {
            'Cantidad_de_Indicios':forms.NumberInput(attrs={'class':'form-control'}),
            'Resguardo_en':forms.Select(attrs={'class':'form-control'}),
            'Carpeta_Investigacion':forms.TextInput(attrs={'class':'form-control'}),
            'Titular':forms.Select(attrs={'class':'form-control'}),
            'Fecha_Ingreso':forms.DateInput(attrs={'class':'form-control'}),
            'Hora_Ingreso':forms.TimeInput(attrs={'class':'form-control'}),
            'Oficio':forms.TextInput(attrs={'class':'form-control'}),

        }

class IndiciosForm(forms.ModelForm):

    class Meta:
        model = Indicio
        fields = [
                'Ingreso_Num',
                'No_Indicio',
                'Tipo',
                'Descripcion',
                'Rue',
                'Clasificacion',
                'Fecha_Caducidad',
                'Peso_Narcotico',
                'Dictamen',
                'Deposito_Banco',
                'Persona_Entrega',
                'Cantidad',
                'Cadena',
                'Embalaje',
                'Estado_embalaje',
                'Ubicacion',
                'Imagen',
                'Observaciones',
                ]
        labels = {
            'Ingreso_Num':'Selecciona la carpeta de Investigación',
            'No_Indicio':'Numero de identificacion del Indicio',
            'Tipo':'Tipo de Indicio (Físico, Orgánico)',
            'Descripcion':'Descripción del Indicios',
            'Rue':' (Rue) Registro Único de Evidencia',
            'Clasificacion':'Clasificacion de Indicio',
            'Fecha_Caducidad': 'Ingresa la Fecha de caducidad solo si es perecedero',
            'Peso_Narcotico': 'Ingresa el peso solo si es Narcotico',
            'Dictamen':'¿Se entrega dictamen de Quimica o de Balistica?',
            'Deposito_Banco': 'Depósito Bancario (Si o No)',
            'Persona_Entrega':'Nombre de la Persona que entrega fisicamente los indicios',
            'Cantidad':'Cantidad solo si es numerio',
            'Cadena':'Cadena de Custodia, Especifique...',
            'Embalaje':'Tipo de Embalaje del Indicio',
            'Estado_embalaje':'Estado del embalaje, especifique...',
            'Ubicacion':'Indique lugar de ubicación del indicio...',
            'Imagen':'Elija la imagen del indicio',
            'Observaciones':'Realice alguna observación acerca del indicio',
                }
        widgets = {
            'Ingreso_Num':forms.Select(attrs={'class':'form-control'}),
            'No_Indicio':forms.TextInput(attrs={'class':'form-control'}),
            'Tipo':forms.Select(attrs={'class':'form-control'}),
            'Descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'Rue':forms.TextInput(attrs={'class':'form-control'}),
            'Clasificacion':forms.Select(attrs={'class':'form-control'}),
            'Fecha_Caducidad':forms.DateInput(attrs={'class':'form-control'}),
            'Peso_Narcotico':forms.NumberInput(attrs={'class':'form-control'}),
            'Dictamen':forms.Select(attrs={'class':'form-control'}),
            'Deposito_Banco':forms.Select(attrs={'class':'form-control'}),
            'Persona_Entrega':forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad':forms.NumberInput(attrs={'class':'form-control'}),
            'Cadena':forms.Select(attrs={'class':'form-control'}),
            'Embalaje':forms.Select(attrs={'class':'form-control'}),
            'Estado_embalaje':forms.Select(attrs={'class':'form-control'}),
            'Ubicacion':forms.TextInput(attrs={'class':'form-control'}),
            'Imagen': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'Observaciones':forms.Textarea(attrs={'class':'form-control'}),
        }
"""
class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salidas
        fields = [
                'Indicio_Numero',
                'Tipo_Movimiento',
                'Fecha_de_Movimiento',
                'Quien_Recibe',
                'Imagen_salida',
        ]
        labels = {
                'Indicio_Numero': 'Rue del Indicio',
                'Tipo_Movimiento': 'Tipo de Movimiento',
                'Fecha_de_Movimiento': 'Fecha de Salida',
                'Quien_Recibe': 'Quién Solicita la Salida',
                'Imagen_salida': 'Foto del Indicio',
        }
        widgets = {
                'Indicio_Numero':forms.Select(attrs={'class':'form-control'}),
                'Tipo_Movimiento':forms.Select(attrs={'class':'form-control'}),
                'Fecha_de_Movimiento':forms.DateInput(attrs={'class':'form-control'}),
                'Quien_Recibe':forms.Select(attrs={'class':'form-control'}),
                'Imagen_salida':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }
"""
class SelExpedienteForm(forms.ModelForm):
    carpeta = forms.ModelChoiceField(
        queryset=Expediente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Indicio 
        fields = ['Ingreso_Num']

class DefForm(forms.ModelForm):
    class Meta:
        model = Definitiva
        fields = [
                'Carpeta',
                'Rue',
                'Fecha_de_Movimiento',
                'Autoridad',
                'Persona_Recibe',
                'Oficio',
                'Sasca',
                'Imagen_salida',
        ]
        labels = {
                'Carpeta': 'Expediente',
                'Rue': 'Rue del Indicio',
                'Fecha_de_Movimiento': 'Fecha de Salida',
                'Autoridad': 'Quién Solicita la Salida',
                'Persona_Recibe': 'Quién recibe el indicio',
                'Oficio': 'Número de Ofico',
                'Sasca': 'Número de Sasca',
                'Imagen_salida': 'Foto de salida definitiva del Indicio',
        }
        widgets = {
                'Carpeta': forms.Select(attrs={'class': 'form-control'}),
                'Rue':forms.Select(attrs={'class':'form-control'}),
                'Fecha_de_Movimiento':forms.DateInput(attrs={'class':'form-control'}),
                'Autoridad':forms.Select(attrs={'class':'form-control'}),
                'Persona_Recibe': forms.TextInput(attrs= {'class': 'form-control'}),
                'Oficio': forms.TextInput(attrs= {'class': 'form-control'}),
                'Sasca': forms.TextInput(attrs= {'class': 'form-control'}),
                'Imagen_salida':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class TemForm(forms.ModelForm):
    class Meta:
        model = Definitiva
        fields = [
                'Carpeta',
                'Rue',
                'Fecha_de_Movimiento',
                'Autoridad',
                'Persona_Recibe',
                'Imagen_salida',
        ]
        labels = {
                'Carpeta': 'Expediente',
                'Rue': 'Rue del Indicio',
                'Fecha_de_Movimiento': 'Fecha de Salida',
                'Autoridad': 'Quién Solicita la Salida',
                'Persona_Recibe': 'Quién recibe el indicio',
                'Imagen_salida': 'Foto de salida temporal del Indicio ',
        }
        widgets = {
                'Carpeta': forms.Select(attrs={'class': 'form-control'}),
                'Rue':forms.Select(attrs={'class':'form-control'}),
                'Fecha_de_Movimiento':forms.DateInput(attrs={'class':'form-control'}),
                'Autoridad':forms.Select(attrs={'class':'form-control'}),
                'Persona_Recibe': forms.TextInput(attrs= {'class': 'form-control'}),
                'Imagen_salida':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class TrasForm(forms.ModelForm):
    class Meta:
        model = Traslado
        fields = [
                'Carpeta',
                'Rue',
                'Fecha_de_Movimiento',
                'Autoridad',
                'Persona_Recibe',
                'Imagen_salida',
        ]
        labels = {
                'Carpeta': 'Expediente',
                'Rue': 'Rue del Indicio',
                'Fecha_de_Movimiento': 'Fecha de Salida',
                'Autoridad': 'Quién Solicita la Salida',
                'Persona_Recibe': 'Quién recibe el indicio',
                'Imagen_salida': 'Foto de salida de traslado del Indicio',
        }
        widgets = {
                'Carpeta': forms.Select(attrs={'class': 'form-control'}),
                'Rue':forms.Select(attrs={'class':'form-control'}),
                'Fecha_de_Movimiento':forms.DateInput(attrs={'class':'form-control'}),
                'Autoridad':forms.Select(attrs={'class':'form-control'}),
                'Persona_Recibe': forms.TextInput(attrs= {'class': 'form-control'}),
                'Imagen_salida':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

