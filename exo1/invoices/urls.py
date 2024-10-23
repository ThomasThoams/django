from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/new/', views.invoice_create, name='invoice_create'),
    path('invoice/<int:pk>/edit/', views.invoice_update, name='invoice_update'),
    path('invoice/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
    path('category/new/', views.category_create, name='category_create'),
    path('client/new/', views.client_create, name='client_create'),
]