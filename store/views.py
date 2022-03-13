from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from perfiles.models import Profile
from products.models import Category

# from .forms import AddToCartForm
from .models import Post

# from .utils import get_or_set_order_session

namespace = 'store'


class HomeView(generic.ListView):
    def get(self, request):
        posts = Post.newmanager.all()
        context = {
            'posts': posts,
        }

        return render(request, 'index.html', context)


class DetalleView(generic.FormView):
    template_name = 'detail.html'
    # form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['post'], status='pb')

    def get_success_url(self):
        return reverse('home')  # TODO: cart

    def form_valid(self, form):
        # order = get_or_set_order_session(self.request)
        product = self.get_object()

        # item_filter = order.items.filter(product=product)

        """ if item_filter.exists():
            item = item_filter.first()
            item.quantity = int(form.cleaned_data['quantity'])
            item.save()
        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save() """

        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DetalleView, self).get_context_data(**kwargs)
        context["product"] = self.get_object()

        return context


class CategoryListView(generic.ListView):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)

        context = {
            'category': category,
            'posts': posts
        }

        return render(request, 'categories.html', context)
