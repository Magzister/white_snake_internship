"""
Module with provile model
"""

from django.db import models
from django.conf import settings

from ..abstract.is_active import IsActive


class Profile(IsActive):
    """
    Represents a user profile with additional information
    """

    SEX_CHOICES = [("M", "Male"), ("F", "Female")]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    driver_license = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.second_name

    class Meta:
        db_table = "profile"
