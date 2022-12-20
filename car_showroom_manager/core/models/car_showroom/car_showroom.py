"""
Module with car showroom model
"""

from django.db import models
from django_countries.fields import CountryField

from ..provider.provider import Provider
from ..abstract.is_active import IsActive


class CarShowroom(IsActive):
    """
    Model to represend information about car showroom
    """

    name = models.CharField(max_length=30)
    location_country = CountryField()
    location_city = models.CharField(max_length=30)
    locarion_street = models.CharField(max_length=30)
    location_house = models.CharField(max_length=30)
    money = models.DecimalField(max_digits=12, decimal_places=2)
    providers = models.ManyToManyField(
        Provider, through="CarShowroomProvider", related_name="car_showrooms"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_showroom"
