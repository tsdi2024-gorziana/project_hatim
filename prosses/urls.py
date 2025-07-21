from django.urls import path
from . import views


urlpatterns = [
    path("generate/",views.generate_file,name="generate"),
    path('dawnloade/<int:id>',views.dawnload_file,name="dawnloade_file"),
    ]