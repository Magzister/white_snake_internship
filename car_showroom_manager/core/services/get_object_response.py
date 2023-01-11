"""
Module with get object as a response service
"""

from typing import Type
from django.db.models import Model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status


ModelType = Type[Model]
SerializerType = Type[Serializer]


def get_object_response(
    serializer: SerializerType, model: ModelType, many: bool = False, **kwargs
) -> Response:
    """Return requested objects as a response"""

    if many:
        _objects = get_list_or_404(model, **kwargs)
        object_serializer = serializer(_objects, many=True)
    else:
        _object = get_object_or_404(model, **kwargs)
        object_serializer = serializer(_object, many=False)
    return Response(object_serializer.data, status=status.HTTP_200_OK)
