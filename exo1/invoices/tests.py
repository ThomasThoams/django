# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Invoice, Client, Category, InvoiceCreationLog
from datetime import date

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")
        self.invoice = Invoice.objects.create(
            name="Test Invoice",
            client=self.client,
            category=self.category,
            amount=100.00,
            description="Test Description",
            date=date.today(),
            paid=False
        )

    def test_invoice_creation(self):
        self.assertEqual(self.invoice.name, "Test Invoice")
        self.assertEqual(self.invoice.client.name, "Test Client")
        self.assertEqual(self.invoice.category.name, "Test Category")
        self.assertEqual(self.invoice.amount, 100.00)
        self.assertFalse(self.invoice.paid)

class InvoiceListViewTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")
        self.invoice1 = Invoice.objects.create(
            name="Invoice 1",
            client=self.client_obj,
            category=self.category,
            amount=150.00,
            description="Description 1",
            date=date.today(),
            paid=False
        )
        self.invoice2 = Invoice.objects.create(
            name="Invoice 2",
            client=self.client_obj,
            category=self.category,
            amount=200.00,
            description="Description 2",
            date=date.today(),
            paid=True
        )

    def test_invoice_list_view(self):
        response = self.client.get(reverse('invoice_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invoice 1")
        self.assertContains(response, "Invoice 2")
        self.assertTemplateUsed(response, 'invoices/invoice_list.html')

    def test_invoice_list_filter_by_client(self):
        response = self.client.get(reverse('invoice_list'), {'client_id': self.client_obj.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invoice 1")
        self.assertContains(response, "Invoice 2")

    def test_invoice_list_filter_by_name(self):
        response = self.client.get(reverse('invoice_list'), {'name': 'Invoice 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invoice 1")
        self.assertNotContains(response, "Invoice 2")

class InvoiceCreateViewTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")

    def test_invoice_create_view(self):
        response = self.client.post(reverse('invoice_create'), {
            'name': 'New Invoice',
            'client': self.client_obj.id,
            'category': self.category.id,
            'amount': 300.00,
            'description': 'New Description',
            'date': date.today(),
            'paid': False
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.first().name, 'New Invoice')

class InvoiceUpdateViewTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")
        self.invoice = Invoice.objects.create(
            name="Invoice to Update",
            client=self.client_obj,
            category=self.category,
            amount=400.00,
            description="Old Description",
            date=date.today(),
            paid=False
        )

    def test_invoice_update_view(self):
        response = self.client.post(reverse('invoice_update', args=[self.invoice.pk]), {
            'name': 'Updated Invoice',
            'client': self.client_obj.id,
            'category': self.category.id,
            'amount': 500.00,
            'description': 'Updated Description',
            'date': date.today(),
            'paid': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.name, 'Updated Invoice')
        self.assertEqual(self.invoice.amount, 500.00)
        self.assertTrue(self.invoice.paid)

class InvoiceDeleteViewTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")
        self.invoice = Invoice.objects.create(
            name="Invoice to Delete",
            client=self.client_obj,
            category=self.category,
            amount=600.00,
            description="Description to delete",
            date=date.today(),
            paid=False
        )

    def test_invoice_delete_view(self):
        response = self.client.post(reverse('invoice_delete', args=[self.invoice.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Invoice.objects.count(), 0)

class InvoiceCreationLogTest(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client", email="test@example.com")
        self.category = Category.objects.create(name="Test Category")

    def test_invoice_creation_log(self):
        invoice = Invoice.objects.create(
            name="Logged Invoice",
            client=self.client_obj,
            category=self.category,
            amount=700.00,
            description="Log this creation",
            date=date.today(),
            paid=False
        )
        log = InvoiceCreationLog.objects.filter(invoice=invoice).first()
        self.assertIsNotNone(log)
        self.assertEqual(log.invoice.name, "Logged Invoice")
