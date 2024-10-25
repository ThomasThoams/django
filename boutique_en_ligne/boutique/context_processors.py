from .models import Categorie

def categories_processor(request):
    categories_parents = Categorie.objects.filter(parent__isnull=True)
    return {'categories_parents': categories_parents}
