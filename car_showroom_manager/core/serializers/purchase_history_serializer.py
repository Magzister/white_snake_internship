"""
Module with purchase history serializer
"""

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from core.models import PurchaseHistory


class PurchaseHistorySerializer(ModelSerializer):
    """
    Purchase history serializer
    """

    car_showroom: PrimaryKeyRelatedField = PrimaryKeyRelatedField()
    vehicle: PrimaryKeyRelatedField = PrimaryKeyRelatedField()

    class Meta:
        model = PurchaseHistory
        fields = [
            "id",
            "car_showroom",
            "vehicle",
            "amount",
            "value",
            "purchase_datetime",
        ]
