"""
Module with abstract IsActive model
"""

from django.db import models


class IsActive(models.Model):
    """
    Abstract class with is_active field to use instead of
    deleting a model from the db.
    """

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
