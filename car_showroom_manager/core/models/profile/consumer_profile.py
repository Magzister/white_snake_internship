"""
Module with consumer profile model
"""

from django.db import models

from core.models.consumer import Consumer
from core.models.abstract.is_active import IsActive


class ConsumerProfile(IsActive):
    """
    Represents a consumer profile with additional information
    """

    SEX_CHOICES = [("M", "Male"), ("F", "Female")]

    consumer = models.OneToOneField(
        Consumer, on_delete=models.CASCADE, related_name="consumer_profile"
    )
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    driver_license = models.BooleanField(default=False)
    money = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.second_name

    class Meta:
        db_table = "consumer_profile"
