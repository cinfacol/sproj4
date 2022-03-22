from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('checkout/', login_required(views.CheckoutView.as_view()), name='checkout'),
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),

]
