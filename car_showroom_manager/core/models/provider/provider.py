"""
Module with provider model
"""

from django.db import models

from ..abstract.is_active import IsActive


class Provider(IsActive):
    """
    Model to represent information about Provider
    """

    name = models.CharField(max_length=30)
    date_of_foundation = models.DateField()
    number_of_buyers = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "provider"
