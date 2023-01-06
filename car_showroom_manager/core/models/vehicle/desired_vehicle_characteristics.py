"""
Module with desired vehicle characteristics of car showroom
"""

from django.db import models

from core.models.abstract import VehicleCharacteristics
from core.models.abstract import IsActive
from core.models.car_showroom import CarShowroom


class DesiredVehicleCharacteristics(VehicleCharacteristics, IsActive):
    """
    Model to represent car showroom's desired vehicle characteristics.
    Use abstract model VehicleCharacteristics
    """

    car_showroom = models.ForeignKey(
        CarShowroom,
        on_delete=models.CASCADE,
        related_name="desired_characteristics",
    )

    class Meta:
        db_table = "desired_vehicle_characteristics"
