from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic import DetailView, FormView, ListView
from products.models import Category

from .models import Post

# from .utils import get_or_set_order_session

namespace = 'store'


class HomeView(ListView):
    queryset = Post.newmanager.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'index.html'


class DetalleView(DetailView):
    template_name = 'detail.html'
    model = Post
    # form_class = AddToCartForm

    def get_context_data(self, *args, **kwargs):
        context = super(DetalleView, self).get_context_data(*args, **kwargs)
        # context["post"] = self.get_object()

        return context


class CategoryListView(ListView):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)

        context = {
            'category': category,
            'posts': posts
        }

        return render(request, 'categories.html', context)
