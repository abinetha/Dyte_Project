# Create your models here.
# json_viewer/models.py
from django.db import models

class LogEntry(models.Model):
    level = models.CharField(max_length=1000)
    message = models.TextField()
    resourceId = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()
    traceId = models.CharField(max_length=1000)
    spanId = models.CharField(max_length=1000)
    commit = models.CharField(max_length=1000)
    parentResourceId = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.level} - {self.message}"
