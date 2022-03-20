from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Address, Profile, UserBase

admin.site.register(UserBase, list_display=(
    'username',
    'email',
    'first_name',
    'last_name',
))
admin.site.register(Address, list_display=(
    'user',
    'residencia_address',
    'oficina_address',
    'address_type',
    'default',
))

admin.site.register(Profile, list_display=(
    'user',
    'picture',
    'phone',
    'bio',
    'verified',
))
