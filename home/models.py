from django.conf import settings
from django.db import models
class Addressrahuhrikte(models.Model):
    'Generated Model'
    street = models.BigIntegerField()
    ca = models.BigIntegerField(null=True,blank=True,)
