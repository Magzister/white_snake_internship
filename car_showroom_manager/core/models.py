from django.db import models


class AttachmentSample(models.Model):
    attachment = models.FileField()
