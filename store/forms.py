from django import forms
# from cart.models import OrderItem
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()


""" class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['quantity'] """
