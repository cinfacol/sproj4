from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.views.decorators.http import require_POST
from perfiles.forms import UserAddressForm
from perfiles.models import Address
from products.models import Product
from store.models import Articulo

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Articulo, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], override_quantity=cd['override'])
    print(product_id)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Articulo, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})


class CheckoutView(generic.FormView):
    template_name = 'cart/checkout.html'
    form_class = UserAddressForm

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        addresses = Address.objects.filter(user=self.request.user)

        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['order'] = cart
        context['addresses'] = addresses
        return context
