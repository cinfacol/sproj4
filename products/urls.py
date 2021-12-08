from django.urls import path

from .views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='products'),
]
