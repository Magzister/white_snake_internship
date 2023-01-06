"""
Module with attachment sample model to test static files management
"""

from django.db import models


class AttachmentSample(models.Model):
    """
    Model to test how static files are managed
    """

    attachment = models.FileField()
