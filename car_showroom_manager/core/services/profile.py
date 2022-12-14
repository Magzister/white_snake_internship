"""
Profile sevices
"""

from typing import Type
from typing import Union
from rest_framework.response import Response

from core.models import ConsumerProfile
from core.models import CarShowroomProfile
from core.models import ProviderProfile
from core.serializers import ConsumerProfileSerializer
from core.serializers import CarShowroomProfileSerializer
from core.serializers import ProviderProfileSerializer


Profile = Union[
    Type[ConsumerProfile], Type[CarShowroomProfile], Type[ProviderProfile]
]
Serializer = Union[
    Type[ConsumerProfileSerializer],
    Type[CarShowroomProfileSerializer],
    Type[ProviderProfileSerializer],
]


def get_profile_response(
    serializer: Serializer, profile: Profile, **kwargs
) -> Response:
    """
    Return response with user's profile
    """
    user_profile = profile.objects.get(**kwargs)
    profile_serializer = serializer(user_profile, many=False)
    return Response(profile_serializer.data)
