"""
Module with model of provider discount for regular customers
"""

from django.db import models

from core.models.provider.provider import Provider
from core.models.abstract import IsActive


class ProviderDiscount(IsActive):
    """
    Model to represent discount for regular customers with number
    of purchases before discount. There can be several discounts for one
    provider: Example. 5% after 500 purchases, 20% after 2000 purchases.
    """

    purchases_before_discount = models.IntegerField()
    discount = models.IntegerField()
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="discounts"
    )

    def __str__(self):
        return str(self.discount) + "%"

    class Meta:
        db_table = "provider_discount"
