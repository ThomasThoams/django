from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Panier(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article, through='PanierArticle')

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"

class PanierArticle(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.article.nom}"
