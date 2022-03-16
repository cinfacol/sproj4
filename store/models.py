from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from inventario.models import Inventory
from mptt.models import TreeManyToManyField
from products.models import Category, Media, Product


class Post(models.Model):

    options = (
        ('upb', 'Unpublished'),
        ('pb', 'Published'),
    )

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='pb')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ForeignKey(
        Media, verbose_name='Producto', on_delete=models.CASCADE)
    inventory = models.ForeignKey(
        Inventory, verbose_name='Inventory', on_delete=models.CASCADE, null=True,
        blank=True)
    category = TreeManyToManyField(Category)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='store_posts', on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(
        max_length=3, choices=options, default='pb')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse("store:detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class ProductFavorite(models.Model):

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
        settings.AUTH_USER_MODEL,
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
        return self.product
