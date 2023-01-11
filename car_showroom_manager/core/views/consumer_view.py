"""
Module with consumer view
"""

from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core.models import Consumer
from core.models import ConsumerProfile
from core.serializers import ConsumerSerializer
from core.serializers import ConsumerProfileSerializer
from core.services import get_object_response
from .custom_viewset import RetrieveUpdateDestroyListVireSet


class ConsumerViewSet(RetrieveUpdateDestroyListVireSet):
    """
    Consumer list generic view set
    """

    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, url_path="profile")
    def get_profile(self, request, pk=None):
        """Return consumer's profile"""

        return get_object_response(
            ConsumerProfileSerializer,
            ConsumerProfile,
            many=False,
            consumer__pk=pk,
        )
