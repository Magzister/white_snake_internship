"""
Module with car showroom profile model
"""

from django.db import models
from django_countries.fields import CountryField

from core.models.car_showroom import CarShowroom
from core.models.abstract.is_active import IsActive


class CarShowroomProfile(IsActive):
    """
    Represents a car showroom profile with additional information
    """

    car_showroom = models.OneToOneField(
        CarShowroom,
        on_delete=models.CASCADE,
        related_name="car_showroom_profile",
    )
    car_showroom_name = models.CharField(max_length=30)
    location_country = CountryField()
    location_city = models.CharField(max_length=30)
    location_street = models.CharField(max_length=30)
    location_house = models.CharField(max_length=30)
    money = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.car_showroom_name

    class Meta:
        db_table = "car_showroom_profile"
