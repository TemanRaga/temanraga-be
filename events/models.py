from django.db import models
from authentication.models import User

# Create your models here.
class Event(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participated_events')
    image = models.ImageField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name