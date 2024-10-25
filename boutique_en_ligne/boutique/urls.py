from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('ajouter-au-panier/<int:pk>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.panier, name='panier'),
    path('retirer-du-panier/<int:pk>/', views.retirer_du_panier, name='retirer_du_panier'),
    path('payer/', views.payer, name='payer'),
    path('compte/', views.compte, name='compte'),
]
