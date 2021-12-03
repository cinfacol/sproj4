from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Address, Profile, UserBase

admin.site.register(UserBase, list_display=(
    'username',
    'first_name',
    'last_name',
    'email',
))
admin.site.register(Address, list_display=(
    'user',
    'residencia_address',
    'oficina_address',
    'address_type',
))

admin.site.register(Profile, DraggableMPTTAdmin, list_display=(
    'tree_actions',
    'indented_title',
    'parent',
    'picture',
    'verified',
))
