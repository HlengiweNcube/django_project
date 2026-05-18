from django.db import models

from inventory.models import Product


class ImportRecord(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    supplier_name = models.CharField(
        max_length=200
    )

    quantity_imported = models.PositiveIntegerField()

    import_date = models.DateField()

    notes = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.product.name} - {self.supplier_name}"