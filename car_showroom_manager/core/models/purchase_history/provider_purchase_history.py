"""
Module with provider purchase history model
"""

from django.db import models

from ..abstract.purchase_history import History
from ..abstract.is_active import IsActive
from ..provider.provider import Provider
from ..provider.provider_vehicle import ProviderVehicle


class ProviderPurchaseHistory(History, IsActive):
    """
    Model to represent purchase history for provider
    """

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="provider_purchase_history",
    )
    vehicle = models.ForeignKey(
        ProviderVehicle,
        on_delete=models.CASCADE,
        related_name="provider_purchase_history",
    )

    class Meta:
        db_table = "provider_purchase_history"
