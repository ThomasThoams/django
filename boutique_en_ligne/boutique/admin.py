from django.contrib import admin
from .models import Categorie, Article

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'parent')
    list_filter = ('parent',)

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article)
