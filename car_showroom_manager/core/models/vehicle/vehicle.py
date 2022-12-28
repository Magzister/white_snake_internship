"""
Module with car showroom vehicle model
"""

from django.db import models
from django.conf import settings

from core.models.abstract import IsActive


class Vehicle(IsActive):
    """
    Model to represent car showroom vehicle. Use Vehicle abstract model
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vehicles",
    )
    model = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return self.model + " " + str(self.value) + " " + str(self.amount)

    class Meta:
        db_table = "car_showroom_vehicle"
