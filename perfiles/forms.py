from django import forms
from mptt.forms import TreeNodeChoiceField

from .models import Address, Profile, UserBase


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["user", "residencia_address",
                  "oficina_address", "ciudad", "departamento", "zip"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["residencia_address"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["oficina_address"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["ciudad"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["departamento"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["zip"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    username = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='Last Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    class Meta:
        model = UserBase
        fields = ('email', 'username', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True


class UserEditExtraForm(forms.ModelForm):

    parent = TreeNodeChoiceField(queryset=Profile.objects.all())
    picture = forms.CharField(
        label='Picture', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Picture', 'id': 'form-picture'}))
    banner = forms.CharField(
        label='Banner', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Banner', 'id': 'form-banner'}))
    url = forms.CharField(
        label='Url', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Url', 'id': 'form-url'}))
    birthday = forms.CharField(
        label='Birthday', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Birthday', 'id': 'form-birthday'}))
    bio = forms.CharField(
        label='Bio', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Bio', 'id': 'form-bio'}))
    phone = forms.CharField(
        label='Phone', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Phone', 'id': 'form-phone'}))
    mobile = forms.CharField(
        label='Mobile', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'mobile', 'id': 'form-mobile'}))

    class Meta:
        model = Profile
        fields = ('parent', 'picture', 'banner',
                  'url', 'birthday', 'bio', 'phone', 'mobile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].widge.attrs.update(
            {'class': 'd-none'}
        )
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
        self.fields['picture'].required = True
        self.fields['phone'].required = True

    def save(self, *args, **kwargs):
        Profile.objects.rebuild()
        return super(UserEditExtraForm, self).save(*args, **kwargs)
