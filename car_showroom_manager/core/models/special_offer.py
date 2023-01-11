"""
Module with special offer model
"""

from django.db import models
from django.conf import settings

from core.models.vehicle import Vehicle
from core.models.abstract import IsActive


class SpecialOffer(IsActive):
    """
    Model to represent special offers.
    Use SpecialOffer abstract class
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="special_offers",
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="special_offers",
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.discount) + "%"

    class Meta:
        db_table = "special_offer"
