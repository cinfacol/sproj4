from django import forms

from .models import OrderItem

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class AddToCartForm(forms.ModelForm):
    # attributes = forms.ChoiceField()
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        model = OrderItem
        fields = ['quantity', 'override']

    """ def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        articulo = Articulo.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        self.fields['name'].queryset = articulo.product.attribute.all() """
