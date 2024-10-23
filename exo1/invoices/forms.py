from django import forms
from .models import Invoice, Category, Client

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name','client', 'category', 'amount', 'description', 'date', 'paid']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']