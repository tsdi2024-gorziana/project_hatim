from django.contrib import admin
from .models import Fiche_descptive

@admin.register(Fiche_descptive)
class FicheDescptiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

