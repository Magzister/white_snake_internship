"""
Module with vehicle characteristics model
"""

from django.db import models


class VehicleCharacteristics(models.Model):
    """
    Abstract model to represent vehicle characteristics
    """

    ENGINE_TYPE_CHOICES = [
        ("P", "Petrol"),
        ("D", "Diesel"),
        ("E", "Electricity"),
    ]

    body_type = models.CharField(max_length=30)
    number_of_seats = models.IntegerField()
    load_capacity = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    engine_type = models.CharField(max_length=1, choices=ENGINE_TYPE_CHOICES)
    max_speed = models.IntegerField()

    def __str__(self):
        characteristics = f"Body type: {self.body_type}\n \
                            Number of seats: {self.number_of_seats}\n \
                            Load capacity: {self.load_capacity}\n \
                            Weight: {self.weight}\n \
                            Engine type: {self.engine_type}\n \
                            Max speed: {self.max_speed}"

        return characteristics

    class Meta:
        abstract = True
