"""
Module with vehicle characteristics serializer
"""

from rest_framework import serializers

from core.models import UserVehicleCharacteristics
from core.models import DesiredVehicleCharacteristics


class VehicleCharacteristicsSerializer(serializers.ModelSerializer):
    """
    Vehicle characteristic serializer
    """

    class Meta:
        model = UserVehicleCharacteristics
        fields = [
            "id",
            "body_type",
            "number_of_seats",
            "load_capacity",
            "weight",
            "engine_type",
            "max_speed",
        ]


class DesiredVehicleCharacteristicsSerializer(serializers.ModelSerializer):
    """
    Desired vehicle characteristic serializer
    """

    class Meta:
        model = DesiredVehicleCharacteristics
        fields = [
            "id",
            "body_type",
            "number_of_seats",
            "load_capacity",
            "weight",
            "engine_type",
            "max_speed",
        ]
