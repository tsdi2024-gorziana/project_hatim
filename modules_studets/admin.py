import nested_admin
from django.contrib import admin
from .models import (
    Filers_modules,
    Seaquesnces_modules,
    Chapitres_sequenses,
    Affectation,
    AffectationSequence,
    AffectationChapitre,
)


# Inline for Chapitre inside Sequence
class AffectationChapitreInline(nested_admin.NestedTabularInline):
    model = AffectationChapitre
    extra = 1
    autocomplete_fields = ['chapitre']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'chapitre':
            try:
                # extract the sequence id from the parent object
                if request._obj_ is not None:
                    sequence = request._obj_.sequence
                    field.queryset = field.queryset.filter(sequenses=sequence)
            except:
                pass
        return field



# Inline for Sequence inside Affectation
class AffectationSequenceInline(nested_admin.NestedTabularInline):
    model = AffectationSequence
    extra = 1
    autocomplete_fields = ['sequence']
    inlines = [AffectationChapitreInline]  # This allows nesting chapitres under sequences


# Main admin for Affectation, with nested inlines for sequences and their chapitres
class AffectationAdmin(nested_admin.NestedModelAdmin):
    model = Affectation
    inlines = [AffectationSequenceInline]
    list_display = ('formateur', 'filiere')
    search_fields = ('formateur__username', 'filiere__name')
    autocomplete_fields = ['formateur', 'filiere', 'modules']


# Register Filers_modules with simple admin view
@admin.register(Filers_modules)
class FilersModulesAdmin(admin.ModelAdmin):
    list_display = ('titer_module', 'referance_uf', 'nbr_sequence', 'heraire_totale')
    search_fields = ('titer_module', 'referance_uf')


# Register Seaquesnces_modules
@admin.register(Seaquesnces_modules)
class SequencesModulesAdmin(admin.ModelAdmin):
    list_display = ('titer_sequence', 'module', 'total_hores')
    search_fields = ('titer_sequence', )
    list_filter = ('module', )


# Register Chapitres_sequenses
@admin.register(Chapitres_sequenses)
class ChapitresSequencesAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sequenses', 'order', 'duree')
    list_filter = ('sequenses', )
    ordering = ('sequenses', 'order')
    search_fields = ('titre', 'description')


# Register the Affectation model with nested admin
admin.site.register(Affectation, AffectationAdmin)
