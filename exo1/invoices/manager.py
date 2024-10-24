# manager.py
from django.db import models

class InvoiceQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(paid=True)

    def unpaid(self):
        return self.filter(paid=False)

class InvoiceManager(models.Manager):
    def get_queryset(self):
        return InvoiceQuerySet(self.model, using=self._db)

    def paid_invoices(self):
        return self.get_queryset().paid()

    def unpaid_invoices(self):
        return self.get_queryset().unpaid()
