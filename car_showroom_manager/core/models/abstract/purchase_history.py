"""
Module with purchase history abstract model
"""

from django.db import models

from core.models.car_showroom.car_showroom import CarShowroom


class History(models.Model):
    """
    Abstract model to represent general information about purchases history
    """

    car_showroom = models.ForeignKey(
        CarShowroom,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_purchase_history",
    )
    amount = models.IntegerField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.car_showroom) + " " + str(self.value)

    class Meta:
        abstract = True
