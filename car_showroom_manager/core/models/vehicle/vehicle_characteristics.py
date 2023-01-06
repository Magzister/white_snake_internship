"""
Module with car showroom vehicle characteristics
"""

from django.db import models

from core.models.abstract import VehicleCharacteristics
from core.models.abstract import IsActive
from core.models.vehicle.vehicle import Vehicle


class UserVehicleCharacteristics(VehicleCharacteristics, IsActive):
    """
    Model represent characteristics of vehicles of car showroom.
    Use abstract model VehicleCharacteristics
    """

    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="characteristics",
    )

    class Meta:
        db_table = "vehicle_characteristics"
