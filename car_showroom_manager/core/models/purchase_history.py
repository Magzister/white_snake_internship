"""
Module with purchase history model
"""

from django.db import models
from django.conf import settings

from core.models.abstract import History
from core.models.abstract import IsActive
from core.models.vehicle import Vehicle


class PurchaseHistory(History, IsActive):
    """
    Model to represent purchase history
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="purchase_history",
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="purchase_history",
    )

    class Meta:
        db_table = "purchase_history"
