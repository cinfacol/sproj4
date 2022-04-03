from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from perfiles.forms import UserAddressForm
from perfiles.models import Address
from store.models import Articulo

from .cart import get_or_set_order_session
from .models import OrderItem


class CartView(generic.TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        cart = context["order"]
        context["post"] = cart.items.all()
        return context


def cart_remove(request, product_id):
    cart = get_or_set_order_session(request)
    product = get_object_or_404(Articulo, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


class CheckoutView(generic.FormView):
    template_name = 'cart/checkout.html'
    form_class = UserAddressForm

    def get_success_url(self):
        return reverse("store:home")  # TODO payment

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)

    def get_context_data(self, *args, **kwargs):
        cart = get_or_set_order_session(self.request)
        addresses = Address.objects.filter(user=self.request.user)

        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['order'] = get_or_set_order_session(self.request)
        # context['cart'] = context['order'].items.all()
        context['addresses'] = addresses
        return context


class IncreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("cart:cart_detail")


class DecreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])

        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("cart:cart_detail")


class RemoveFromCartView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("cart:cart_detail")
