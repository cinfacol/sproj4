from django.shortcuts import get_object_or_404, render
from django.views import generic
from perfiles.models import Profile

from .models import Category, Media, Product

namespace = "products"


class ProductListView(generic.ListView):

    model = Media

    def get(self, request):
        media = Media.objects.all()
        # products = Product.image_product # reverse muchos a uno entre Product db y Media db

        context = {
            "media": media,
        }

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)

            context = {
                "media": media,
                "profile": profile,
            }

        return render(request, "products/product_list.html", context)


class ProductDetailView(generic.DetailView):

    model = Media
    template_name = "products/product_detail.html"

    if Profile.objects.get().user.is_authenticated:

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["profile"] = Profile.objects.get()

            return context
