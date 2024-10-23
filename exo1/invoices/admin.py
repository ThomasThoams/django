from django.contrib import admin
from .models import Invoice

def mark_as_paid(modeladmin, request, queryset):
    queryset.update(status='paid')  # Assurez-vous que 'status' est un champ de votre modèle Invoice
    modeladmin.message_user(request, "Selected invoices have been marked as paid.")

mark_as_paid.short_description = "Mark selected invoices as paid"

class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ['client', 'name']
    actions = [mark_as_paid]

admin.site.register(Invoice, InvoiceAdmin)
