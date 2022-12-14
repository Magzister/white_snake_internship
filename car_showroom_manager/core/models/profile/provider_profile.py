"""
Module with provider profile model
"""

from django.db import models

from core.models.provider import Provider
from core.models.abstract.is_active import IsActive


class ProviderProfile(IsActive):
    """
    Model to represent information about Provider
    """

    provider = models.OneToOneField(
        Provider, on_delete=models.CASCADE, related_name="provider_profile"
    )
    provider_name = models.CharField(max_length=30)
    date_of_foundation = models.DateField()
    number_of_buyers = models.IntegerField()

    def __str__(self):
        return self.provider_name

    class Meta:
        db_table = "provider_profile"
