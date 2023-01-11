"""
Module with vehicle serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import Vehicle


class VehicleSerializer(ModelSerializer):
    """
    Vehicle serializer
    """

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "model",
            "value",
            "amount",
        ]
