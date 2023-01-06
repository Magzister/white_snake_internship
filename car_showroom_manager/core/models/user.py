"""
Module with User model to respresent several user types
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model with several user types
    """

    class Types(models.TextChoices):
        """
        Class with test choices as a type of user
        """

        CONSUMER = "CONSUMER", "consumer"
        CAR_SHOWROOM = "CAR_SHOWROOM", "car showroom"
        PROVIDER = "PROVIDER", "provider"

    user_type = models.CharField(
        max_length=12, choices=Types.choices, default=Types.CONSUMER
    )

    car_showroom_provider_m2m = models.ManyToManyField(
        "self",
        through="CarShowroomProvider",
    )
