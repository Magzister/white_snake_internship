"""
Module with car showroom vehicle characteristics
"""

from django.db import models

from ..abstract.vehicle_characteristics import VehicleCharacteristics
from ..abstract.is_active import IsActive
from .car_showroom_vehicle import CarShowroomVehisle


class CarShowroomVehicleCharacteristics(VehicleCharacteristics, IsActive):
    """
    Model represent characteristics of vehicles of car showroom.
    Use abstract model VehicleCharacteristics
    """

    vehicle = models.OneToOneField(
        CarShowroomVehisle,
        on_delete=models.CASCADE,
        related_name="characteristics"
    )

    class Meta:
        db_table = "car_showroom_vehicle_characteristics"
