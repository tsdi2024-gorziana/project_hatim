from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from prosses.models import Fiche_descptive
from modules_studets.models import  Affectation, Filers_modules, Seaquesnces_modules, Chapitres_sequenses, AffectationSequence, AffectationChapitre
# Create your views here.

@login_required(login_url='login')
def formater_dach(request):
    user = request.user
    affectation = Affectation.objects.filter(formateur=user).all()




    context = {
        'user': user,
        'affectations': affectation,

    }
    return render(request, 'dechbords/formater_dach.html', context)
@login_required(login_url='login')
def fiche_desqreptive(request, affectation_id, module_id):
    user = request.user

    # Get the correct affectation of this user
    affectation = get_object_or_404(Affectation, id=affectation_id, formateur=user)

    # Make sure the module is part of this affectation
    module = get_object_or_404(affectation.modules, id=module_id)

    # Sequences for this module
    affectation_sequences = AffectationSequence.objects.filter(
        affectation=affectation,
        sequence__module=module
    )

    # Chapitres for those sequences
    chapitres = AffectationChapitre.objects.filter(
        affectation_sequence__in=affectation_sequences
    ).select_related('chapitre')



    context = {
        'user': user,
        'affectation': affectation,
        'module': module,
        'sequences': [a_seq.sequence for a_seq in affectation_sequences],
        'chapitres': [a_chap.chapitre for a_chap in chapitres],
    }

    return render(request, 'dechbords/fiche_desqreprive.html', context)

@login_required
def dashboard_admin(request):
    all_files = Fiche_descptive.objects.all().select_related('user', 'filer', 'module')
    return render(request, 'dechbords/administration_dach.html', {'all_files': all_files})
