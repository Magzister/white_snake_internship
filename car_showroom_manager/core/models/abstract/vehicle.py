"""
Module with vehicle model
"""

from django.db import models


class Vehicle(models.Model):
    """
    Abstract model to represent general information about vehicles of
    car showrooms and providers
    """

    model = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return self.model + " " + str(self.value) + " " + str(self.amount)

    class Meta:
        abstract = True
