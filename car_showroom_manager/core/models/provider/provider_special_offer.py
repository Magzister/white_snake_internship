"""
Module with provider special offer model
"""

from django.db import models

from .provider import Provider
from .provider_vehicle import ProviderVehicle
from ..abstract.special_offer import SpecialOffer
from ..abstract.is_active import IsActive


class ProviderSpecialOffer(SpecialOffer, IsActive):
    """
    Model to represent provider's special offers.
    Use SpecialOffer abstract class
    """

    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="special_offers"
    )
    vehicle = models.ForeignKey(
        ProviderVehicle,
        on_delete=models.CASCADE,
        related_name="special_offers",
    )

    class Meta:
        db_table = "provider_special_offer"
