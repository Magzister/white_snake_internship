"""
Module with user purchase history model
"""

from django.db import models
from django.conf import settings

from ..abstract.purchase_history import History
from ..abstract.is_active import IsActive
from ..car_showroom.car_showroom_vehicle import CarShowroomVehisle


class UserPurchaseHistory(History, IsActive):
    """
    Model to represent purchase history for user
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_purchase_history",
    )
    vehicle = models.ForeignKey(
        CarShowroomVehisle,
        on_delete=models.CASCADE,
        related_name="user_purchase_history",
    )

    class Meta:
        db_table = "user_purchase_history"
