from django.conf import settings
from django.db import models
from perfiles.models import Address, UserBase
from store.models import Post


class OrderItem(models.Model):
    order = models.ForeignKey(
        "order", related_name='item', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.inventory.product.name}"


class Order(models.Model):
    user = models.ForeignKey(
        UserBase, verbose_name=("order_user"), on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"{self.pk}"


class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.PROTECT, related_name='payments')
    payment_method = models.CharField(
        max_length=20, choices=(('Paypal', 'Paypal'),))
    timestamp = models.DateTimeField(auto_now_add=True)
    succesful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"
