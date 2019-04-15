from django.contrib import admin
from Dba.Apps.Boveda.models import *
#from import_export.admin import ImportExportModelAdmin


#admin.site.register(Mp)
admin.site.register(Temporal)
admin.site.register(Definitiva)
admin.site.register(Traslado)
admin.site.register(Rue)

class Indicioinline(admin.TabularInline):
    model = Indicio

		
@admin.register(Mp) 
class MpAdmin(admin.ModelAdmin):
    list_filter = ('Adscripcion','Cargo')
    list_display = ('Nombre','Adscripcion','Cargo')
    ordering = ('Nombre',)
    search_fields = ('Nombre',)
    fields = ['Nombre', ('Adscripcion', 'Cargo')]
    

@admin.register(Indicio)
class IndicioAdmin(admin.ModelAdmin):
	list_filter = ('Clasificacion','Ingreso_Num','Deposito_Banco',)
	list_display = ('Rue','Ingreso_Num','Descripcion','Clasificacion','Deposito_Banco','Cantidad')
	search_fields = ('Clasificacion','Descripcion','Rue',)
#fields = ['Ingreso_Num', ('Rue','Tipo','No_Indicio','Descripcion','Imagen'),'Clasificacion',('Deposito_Banco','Cantidad','Fecha_Caducidad','Peso_Narcotico','Dictamen'),'Embalaje',('Estado_emablaje','Ubicacion','Observaciones')]
#fields = ['Ingreso_Num', ('Rue','Tipo','No_Indicio','Descripcion','Imagen')]
	#inlines = [Expedienteinline]

@admin.register(Expediente) 
class ExpedienteAdmin(admin.ModelAdmin):
    list_filter = ('Resguardo_en','Titular_id')
    list_display = ('Carpeta_Investigacion','Fecha_Ingreso','Resguardo_en')
    #ordering = ('Carpeta_Investigacion',)
    search_fields = ('Carpeta_Investigacion',)
    inlines = [Indicioinline]

"""@admin.register(Salidas) 
class SalidasAdmin(admin.ModelAdmin):
    list_filter = ('Tipo_Movimiento','Quien_Recibe')
    list_display = ('Tipo_Movimiento','Indicio_Numero_id','Fecha_de_Movimiento')
    ordering = ('Fecha_de_Movimiento',)
    search_fields = ('Indicio_Numero_id',)



class IndicioResource(resources.ModelResource):

    class Meta:
        model = Indicio

        fields = ('Rue', 'Descripcion', 'Deposito_Banco', 'Cantidad',)
        export_order = ('id', 'Rue', 'Descripcion', 'Clasificacion','Deposito_Banco','Cantidad',)


class IndiAdmin(ImportExportModelAdmin):
    resource_class = IndicioResource
"""
