from django.urls import path
from . import views


urlpatterns = [
    path('dachbord/',views.formater_dach,name='dach_formater'),
    path('dachbord/administration/',views.dashboard_admin,name='adinistration_dach'),
    path('dachbord/genereat/<int:affectation_id>/<int:module_id>/',views.fiche_desqreptive,name='fiche_desqreptive'),

]