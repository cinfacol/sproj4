from django.shortcuts import render
from django.views import generic
from perfiles.models import Profile

from .models import Media, Product

namespace = 'products'


class ProductListView(generic.ListView):
    model = Product
    model = Media

    def get(self, request):
        products = Media.objects.all()

        context = {
            'products': products,
        }

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            print(products)

            context = {
                'products': products,
                'profile': profile,
            }

        return render(request, 'products/product_list.html', context)


class ProductDetailView(generic.DetailView):

    def get(self, request):

        context = {}

        return render(request, 'products/product_detail.html', context)
