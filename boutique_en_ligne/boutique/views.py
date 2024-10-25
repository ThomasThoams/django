from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Categorie, Panier, PanierArticle
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def accueil(request):
    categories_parents = Categorie.objects.filter(parent__isnull=True)
    categorie_id = request.GET.get('categorie')
    if categorie_id:
        categorie_selectionnee = Categorie.objects.get(id=categorie_id)
        articles = Article.objects.filter(categorie__in=categorie_selectionnee.get_descendants(include_self=True))
    else:
        articles = Article.objects.all()
    return render(request, 'boutique/accueil.html', {
        'articles': articles,
        'categories_parents': categories_parents,
    })


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            Panier.objects.create(utilisateur=user)
            login(request, user)
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'boutique/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
    return render(request, 'boutique/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('accueil')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'boutique/article_detail.html', {'article': article})

@login_required
def ajouter_au_panier(request, pk):
    article = get_object_or_404(Article, pk=pk)
    panier = request.user.panier
    panier_article, created = PanierArticle.objects.get_or_create(panier=panier, article=article)
    if not created:
        panier_article.quantite += 1
        panier_article.save()
    return redirect('panier')

@login_required
def panier(request):
    panier = request.user.panier
    articles = panier.panierarticle_set.all()
    total = sum([item.article.prix * item.quantite for item in articles])
    return render(request, 'boutique/panier.html', {'articles': articles, 'total': total})

@login_required
def retirer_du_panier(request, pk):
    article = get_object_or_404(Article, pk=pk)
    panier = request.user.panier
    panier_article = get_object_or_404(PanierArticle, panier=panier, article=article)
    panier_article.delete()
    return redirect('panier')

@login_required
def payer(request):
    panier = request.user.panier
    panier.panierarticle_set.all().delete()
    return redirect('accueil')

@login_required
def compte(request):
    return render(request, 'boutique/compte.html')
