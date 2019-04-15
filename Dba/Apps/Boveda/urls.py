from django.conf.urls import url, include
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


from Dba.Apps.Boveda.views import index, mp_view, mp_list, mp_edit, mp_delete,Autoridadlist,AutoridadCreate,AutoridadUpdateView,AutoridadDeleteView,ExpedienteCreate,ExpedienteList,ExpedienteUpdateView,IndicioCreate,IndicioList,IndicioUpdateView,mis_indicios
from Dba.Apps.Boveda.views import ReporteIndicios,indicioscarpeta,buscacarpeta, buscar, DefinitivaCreate, DefinitivaList,DefinitivaUpdateView, TemporalCreate, TemporalList, TemporalUpdateView
from Dba.Apps.Boveda.views import TrasladoCreate, TrasladoList, TrasladoUpdateView, ReporteTraslado, ReporteDefinitiva, logout_view


urlpatterns = [
    url(r'^$',LoginView.as_view(template_name='boveda/login.html'),name='login'),
    url(r'^index/$', index, name= 'index'),
    url(r'^cerrar/$',logout_view,name='logout'),
    url(r'^nuevo$', AutoridadCreate.as_view(), name='autoridad_alta'),
    url(r'^listar$', Autoridadlist.as_view(), name='autoridad_listar'),
    url(r'^editar/(?P<pk>\d+)/$', AutoridadUpdateView.as_view(), name='autoridad_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', AutoridadDeleteView.as_view(), name='autoridad_eliminar'),
    url(r'^nuevo_exp$', ExpedienteCreate.as_view(), name='expediente_alta'),
    url(r'^lista_exp$', ExpedienteList.as_view(), name='expediente_listar'),
    url(r'^editar_exp/(?P<pk>\d+)/$', ExpedienteUpdateView.as_view(), name='expediente_editar'),
    url(r'^nuevo_ind$', IndicioCreate.as_view(), name='indicio_alta'),
    url(r'^lista_ind$', IndicioList.as_view(), name='indicio_listar'),
    url(r'^editar_ind/(?P<pk>\d+)/$', IndicioUpdateView.as_view(), name='indicio_editar'),
    url(r'^indicios/(?P<q>\d+)/$', mis_indicios, name='mis_indicios'),
    url(r'^excel$', ReporteIndicios.as_view(), name='reporte_indicios_excel'),
    url(r'^buscar_carpeta$', buscacarpeta, name='buscar_carpeta'),
    url(r'^buscar/$', buscar),
    url(r'^nuevo_def$', DefinitivaCreate.as_view(), name='def_alta'),
    url(r'^lista_def$', DefinitivaList.as_view(), name='def_listar'),
    url(r'^editar_def/(?P<pk>\d+)/$', DefinitivaUpdateView.as_view(), name='def_editar'),
    url(r'^nuevo_tem$', TemporalCreate.as_view(), name='tem_alta'),
    url(r'^lista_tem$', TemporalList.as_view(), name='tem_listar'),
    url(r'^editar_tem/(?P<pk>\d+)/$', TemporalUpdateView.as_view(), name='tem_editar'),
    url(r'^nuevo_tras$', TrasladoCreate.as_view(), name='tras_alta'),
    url(r'^lista_tras$', TrasladoList.as_view(), name='tras_listar'),
    url(r'^editar_tras/(?P<pk>\d+)/$', TrasladoUpdateView.as_view(), name='tras_editar'),
    url(r'^reporte_tras$', ReporteTraslado.as_view(), name='reporte_traslado_excel'),
    url(r'^reporte_def$', ReporteDefinitiva.as_view(), name='reporte_definitiva_excel'),      
]



