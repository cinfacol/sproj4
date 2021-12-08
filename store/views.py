from django.shortcuts import render
from django.views import generic
from products.models import Category


class HomeView(generic.ListView):
    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            profile = request.user.profile

            context = {
                'profile': profile,
            }

        return render(request, 'index.html', context)
