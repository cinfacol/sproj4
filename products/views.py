from django.shortcuts import render
from django.views import generic

from .models import Product

namespace = "products"


class ProductListView(generic.ListView):

    model = Product

    def get(self, request):
        media = Product.objects.all()

        context = {
            "media": media,
        }

        return render(request, "products/product_list.html", context)


class MediaDetailView(generic.DetailView):

    model = Product
    template_name = "products/product_detail.html"
