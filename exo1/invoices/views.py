from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, Category, Client
from .forms import InvoiceForm, CategoryForm, ClientForm

def invoice_list(request):
    client_id = request.GET.get('client')
    name_query = request.GET.get('name')
    clients = Client.objects.all()
    
    invoices = Invoice.objects.all()
    
    if client_id:
        invoices = invoices.filter(client_id=client_id)
    
    if name_query:
        invoices = invoices.filter(name__icontains=name_query)
    
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices, 'clients': clients})



def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})

def invoice_create(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            if not invoice.category:
                other_category, created = Category.objects.get_or_create(name="Autres")
                invoice.category = other_category
            invoice.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoices/invoice_form.html', {'form': form})

def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            if not invoice.category:
                other_category, created = Category.objects.get_or_create(name="Autres")
                invoice.category = other_category
            invoice.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoices/invoice_form.html', {'form': form})

def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == "POST":
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_confirm_delete.html', {'invoice': invoice})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = CategoryForm()
    return render(request, 'invoices/category_form.html', {'form': form})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = ClientForm()
    return render(request, 'invoices/client_form.html', {'form': form})

def paid_invoices_view(request):
    paid_invoices = Invoice.objects.paid_invoices()
    return render(request, 'invoices/paid_invoices.html', {'invoices': paid_invoices})

def unpaid_invoices_view(request):
    unpaid_invoices = Invoice.objects.unpaid_invoices()
    return render(request, 'invoices/unpaid_invoices.html', {'invoices': unpaid_invoices})