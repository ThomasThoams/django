# middleware.py
from .models import Invoice, InvoiceCreationLog

class InvoiceCreationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == "POST" and "/invoice/create/" in request.path:
            invoice_id = response.context_data.get('invoice_id') if hasattr(response, 'context_data') else None
            if invoice_id:
                invoice = Invoice.objects.get(pk=invoice_id)
                InvoiceCreationLog.objects.create(invoice=invoice)

        return response
