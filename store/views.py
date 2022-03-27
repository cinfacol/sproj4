from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from products.models import Category, Media

from .models import Articulo

namespace = 'store'


class HomeView(ListView):
    queryset = Articulo.newmanager.all()
    paginate_by = 4
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        qs = Articulo.newmanager.filter(
            inventory__products__imagenes__default=True)
        images = Articulo.newmanager.filter()
        context = super(HomeView, self).get_context_data(**kwargs)
        context["articulos"] = qs
        print(qs)
        return context


class DetalleView(DetailView):
    template_name = 'detail.html'
    model = Articulo
    cart_product_form = CartAddProductForm()

    def get_context_data(self, *args, **kwargs):
        context = super(DetalleView, self).get_context_data(*args, **kwargs)
        context["post"] = self.get_object()
        context["cart_product_form"] = self.cart_product_form

        return context


class CategoryListView(ListView):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        articulos = Articulo.newmanager.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            articulos = Articulo.objects.filter(category=category)

        context = {
            'category': category,
            'categories': categories,
            'articulos': articulos
        }

        return render(request, 'categories.html', context)
