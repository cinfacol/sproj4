from django.db import models
from django.urls import reverse
from django.utils import timezone
from inventario.models import Inventory
from perfiles.models import UserBase


class Articulo(models.Model):

    options = (
        ('upb', 'Unpublished'),
        ('pb', 'Published'),
    )

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='pb')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')

    published = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        UserBase, related_name='vendedor', on_delete=models.CASCADE)
    inventory = models.OneToOneField(
        Inventory, related_name="inventorys", on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(
        max_length=3, choices=options, default='pb')

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse("store:detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-published',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title


""" class ProductFavorite(models.Model):

    FAVORITE_STATUS = (
        ('AC', 'Publicación activa'),
        ('PP', 'Publicación pausada'),
        ('ND', 'Producto No disponible'),
        ('PA', 'Producto Agotado'),
        ('PR', 'Producto rebajado'),
        ('EG', 'Envío gratis'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        UserBase,
        related_name='favorite_client',
        on_delete=models.CASCADE,
    )
    status = models.CharField(choices=FAVORITE_STATUS,
                              max_length=2, default='AC')
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="format: Y-m-d H:M:S",
    )

    def __str__(self):
        return self.product """
