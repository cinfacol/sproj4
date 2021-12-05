from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import (get_object_or_404, redirect, render)
from django.urls import reverse
from django.views.generic import DetailView, View
from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from .forms import UserAddressForm, UserEditExtraForm, UserEditForm
from .models import Address, Profile, UserBase

User = get_user_model()


class UserProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(UserBase, username=username)
        profile = Profile.objects.get(user=user)
        addresses = Address.objects.filter(user=user, default=True)

        context = {
            'user': user,
            'profile': profile,
            "addresses": addresses,
        }
        return render(request, 'perfiles/detail.html', context)


@login_required
def edit_details(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
        else:
            print('Error en la validación del formulario')
    else:
        user_form = UserEditForm(instance=request.user)

    user = get_object_or_404(UserBase, username=request.user)
    profile = Profile.objects.get(user=user)

    context = {
        'user_form': user_form,
        'profile': profile,
    }

    return render(request, 'perfiles/edit_profile.html', context)


@login_required
def edit_extra_details(request):
    user_extra_form = UserEditExtraForm(
        instance=request.user, data=request.POST)
    if request.method == 'POST':
        form = MoveNodeForm(user_extra_form, request.POST)
        print(user_extra_form)

        if form.is_valid():
            try:
                user_extra_form = form.save()
                return HttpResponseRedirect(user_extra_form.get_absolute_url())
            except InvalidMove:
                pass
    else:
        form = MoveNodeForm(user_extra_form)

    context = {
        'form': form,
        'user_extra_form': user_extra_form,
        'user_extra_tree': user_extra_form.objects.all(),
    }

    return render('perfiles/edit_extra_profile.html', context)

# Addresses


@login_required
def view_address(request):
    addresses = Address.objects.filter(user=request.user)
    profile = Profile.objects.get(user=request.user)
    context = {
        "addresses": addresses,
        'profile': profile,
    }
    return render(request, "perfiles/addresses.html", context)


@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.user = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("perfiles:direcciones"))
    else:
        address_form = UserAddressForm()
    return render(request, "perfiles/edit_addresses.html", {"form": address_form})


@login_required
def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(pk=id, user=request.user)
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("perfiles:direcciones"))
    else:
        address = Address.objects.get(pk=id, user=request.user)
        address_form = UserAddressForm(instance=address)
    return render(request, "perfiles/edit_addresses.html", {"form": address_form})


@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, user=request.user).delete()
    return redirect("perfiles:direcciones")


@login_required
def set_default(request, id):
    Address.objects.filter(user=request.user,
                           default=True).update(default=False)
    Address.objects.filter(pk=id, user=request.user).update(default=True)
    return redirect("perfiles:direcciones")
