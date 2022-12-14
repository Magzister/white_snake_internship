"""
Module with car showroom profile serializer
"""

from rest_framework.serializers import ModelSerializer
from django_countries.serializer_fields import CountryField

from core.models import CarShowroomProfile


class CarShowroomProfileSerializer(ModelSerializer):
    """
    Car showroom profile serializer
    """

    location_country = CountryField()

    class Meta:
        model = CarShowroomProfile
        fields = [
            "id",
            "car_showroom_name",
            "location_country",
            "location_city",
            "location_street",
            "location_house",
            "money",
        ]
