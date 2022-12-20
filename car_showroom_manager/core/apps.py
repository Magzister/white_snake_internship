"""
Module with app configs
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Config for core app
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
