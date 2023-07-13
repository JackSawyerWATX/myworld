from django.db import models

class Record(models.Model):
  artist = models.CharField(max_length=255)
  album = models.CharField(max_length=255)
  record_label = models.CharField(null=True, max_length=255)
  released = models.DateField(null=True)