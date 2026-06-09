from django.db import models
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP

from inventory.models import Product


CENTS = Decimal('0.01')


def get_default_tax_rate():
    return Decimal(str(getattr(settings, 'DEFAULT_TAX_RATE', '0.15')))


class ExportRecord(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(
        max_length=200
    )

    quantity_exported = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    subtotal_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00')
    )

    tax_rate = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        default=get_default_tax_rate
    )

    tax_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00')
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00')
    )

    export_date = models.DateField()

    notes = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        unit_price = Decimal(self.product.price or Decimal('0.00'))
        quantity = Decimal(self.quantity_exported or 0)
        tax_rate = Decimal(self.tax_rate if self.tax_rate is not None else get_default_tax_rate())

        self.unit_price = unit_price.quantize(CENTS, rounding=ROUND_HALF_UP)
        self.subtotal_amount = (self.unit_price * quantity).quantize(CENTS, rounding=ROUND_HALF_UP)
        self.tax_rate = tax_rate
        self.tax_amount = (self.subtotal_amount * self.tax_rate).quantize(CENTS, rounding=ROUND_HALF_UP)
        self.total_amount = (self.subtotal_amount + self.tax_amount).quantize(CENTS, rounding=ROUND_HALF_UP)

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.product.name} - {self.customer_name}"