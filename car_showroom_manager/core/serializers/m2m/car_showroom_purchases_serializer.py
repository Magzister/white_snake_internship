"""
Module with provider purchase serializer
"""

from rest_framework.serializers import ModelSerializer

from core.models import CarShowroomProvider
from core.serializers.car_showroom_serializer import CarShowroomSerializer


class CarShowroomPurchasesSerializer(ModelSerializer):
    """
    CarShowroom purchase serializer
    """

    car_showroom = CarShowroomSerializer(many=False)

    class Meta:
        model = CarShowroomProvider
        fields = [
            "car_showroom",
            "number_of_purchases",
        ]
