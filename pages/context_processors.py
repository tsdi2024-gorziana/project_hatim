from modules_studets.models import Affectation
from prosses.models import Fiche_descptive

def affectations_processor(request):
    if request.user.is_authenticated:
        affectations = Affectation.objects.filter(formateur=request.user).all()
    else:
        affectations = []
    return {
        'affectations': affectations
    }
def files_processor(request):
    if request.user.is_authenticated:
        files = Fiche_descptive.objects.filter(user=request.user).all()
    else:
        files = []
    return {
        'files': files
    }
