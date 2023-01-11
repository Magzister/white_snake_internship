"""
Module with consumer profile serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import ConsumerProfile


class ConsumerProfileSerializer(ModelSerializer):
    """
    Consumer profile serializer
    """

    class Meta:
        model = ConsumerProfile
        fields = [
            "id",
            "first_name",
            "second_name",
            "age",
            "sex",
            "driver_license",
            "money",
        ]
