"""
Module with car showroom special offer model
"""

from django.db import models

from .car_showroom import CarShowroom
from .car_showroom_vehicle import CarShowroomVehisle
from ..abstract.special_offer import SpecialOffer
from ..abstract.is_active import IsActive


class CarShowroomSpecialOffer(SpecialOffer, IsActive):
    """
    Model to represent car showroom's special offers.
    Use SpecialOffer abstract class
    """

    car_showroom = models.ForeignKey(
        CarShowroom, on_delete=models.CASCADE, related_name="special_offers"
    )
    vehicle = models.ForeignKey(
        CarShowroomVehisle,
        on_delete=models.CASCADE,
        related_name="special_offers",
    )

    class Meta:
        db_table = "car_showroom_special_offer"
