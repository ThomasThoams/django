from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Categorie, Article

class CategorieAdmin(MPTTModelAdmin):
    pass

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article)
