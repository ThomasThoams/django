from django.db import models
from .manager import InvoiceManager

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
    paid = models.BooleanField(default=False)
    objects = InvoiceManager()
    def __str__(self):
        return f"Invoice {self.id} - {self.client.name}"

class InvoiceCreationLog(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice Log for {self.invoice.name} at {self.created_at}"
