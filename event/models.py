from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    date = models.DateTimeField()
    createdBy = models.CharField(max_length=225)
