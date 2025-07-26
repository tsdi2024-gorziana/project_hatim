from django.contrib import admin
from .models import AcademicYear, Filieres

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'annee')
    search_fields = ('name', 'annee')


@admin.register(Filieres)
class FilieresAdmin(admin.ModelAdmin):
    list_display = ('title', 'academic_year')
    list_filter = ('academic_year',)
    search_fields = ('title',)
    filter_horizontal = ("formateurs",)
