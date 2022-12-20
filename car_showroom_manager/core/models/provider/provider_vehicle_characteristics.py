"""
Module with provider vehicle characteristics model
"""

from django.db import models

from ..abstract.vehicle_characteristics import VehicleCharacteristics
from ..abstract.is_active import IsActive
from .provider_vehicle import ProviderVehicle


class ProviderVehicleCharacteristics(VehicleCharacteristics, IsActive):
    """
    Model represent characteristics of vehicle of provider.
    Use abstract model VehicleCharacteristic
    """

    vehicle = models.OneToOneField(
        ProviderVehicle,
        on_delete=models.CASCADE,
        related_name="characteristics"
    )

    class Meta:
        db_table = "provider_vehicle_characteristics"
