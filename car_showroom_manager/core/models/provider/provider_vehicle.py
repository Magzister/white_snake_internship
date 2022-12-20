"""
Module with provider vehicle model
"""

from django.db import models

from .provider import Provider
from ..abstract.vehicle import Vehicle
from ..abstract.is_active import IsActive


class ProviderVehicle(Vehicle, IsActive):
    """
    Model to represent provider vehicle. Use Vehicle abstract model
    """

    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="vehicles"
    )

    class Meta:
        db_table = "provider_vehicle"
