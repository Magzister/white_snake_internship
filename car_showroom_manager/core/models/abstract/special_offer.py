"""
Module with special offer model
"""

from django.db import models


class SpecialOffer(models.Model):
    """
    Abstract model to represent general information about special offers
    and discounts of car showrooms and providers
    """

    name = models.CharField(max_length=30)
    description = models.TextField()
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    discount = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.discount) + "%"

    class Meta:
        abstract = True
