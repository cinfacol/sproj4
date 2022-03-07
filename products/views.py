from django.shortcuts import render
from django.views import generic

from .models import Media

namespace = "products"


class ProductListView(generic.ListView):

    model = Media

    def get(self, request):
        media = Media.objects.all()

        context = {
            "media": media,
        }

        return render(request, "products/product_list.html", context)


class MediaDetailView(generic.DetailView):

    model = Media
    template_name = "products/product_detail.html"
