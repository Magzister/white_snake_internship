"""
Module woth car_showroom_provider table that represent m2m relation
with additional information about number of purchases
"""

from django.db import models

from core.models.car_showroom import CarShowroom
from core.models.provider import Provider
from core.models.abstract import IsActive


class CarShowroomProvider(IsActive):
    """
    Model to represent m2m relation between car showroom and provider
    with additional information as number of purchases
    """

    car_showroom = models.ForeignKey(
        CarShowroom, on_delete=models.CASCADE, related_name="car_showroom_user"
    )
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="provider_user"
    )
    number_of_purchases = models.IntegerField()

    def __str__(self):
        return (
            str(self.car_showroom)
            + " "
            + str(self.provider)
            + " "
            + str(self.number_of_purchases)
        )

    class Meta:
        db_table = "car_showroom_provider"
