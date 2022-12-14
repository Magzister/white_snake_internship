"""
Module with car showroom serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import CarShowroom


class CarShowroomSerializer(ModelSerializer):
    """
    Car showroom serializer
    """

    class Meta:
        model = CarShowroom
        fields = [
            "id",
            "username",
            "email",
        ]
