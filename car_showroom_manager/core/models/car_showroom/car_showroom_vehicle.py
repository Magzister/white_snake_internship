"""
Module with car showroom vehicle model
"""

from django.db import models

from .car_showroom import CarShowroom
from ..abstract.vehicle import Vehicle
from ..abstract.is_active import IsActive


class CarShowroomVehisle(Vehicle, IsActive):
    """
    Model to represent car showroom vehicle. Use Vehicle abstract model
    """

    car_chowroom = models.ForeignKey(
        CarShowroom, on_delete=models.CASCADE, related_name="vehicles"
    )

    class Meta:
        db_table = "car_showroom_vehicle"
