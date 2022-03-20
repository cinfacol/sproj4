from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from products.models import Category

from .models import Post

namespace = 'store'


class HomeView(ListView):
    queryset = Post.newmanager.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'index.html'


class DetalleView(DetailView):
    template_name = 'detail.html'
    model = Post
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
        posts = Post.newmanager.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            posts = Post.objects.filter(category=category)

        context = {
            'category': category,
            'categories': categories,
            'posts': posts
        }

        return render(request, 'categories.html', context)
