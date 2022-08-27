from django.db import models
from authentication.models import User
import datetime
from django.utils.translation import gettext as _

# Create your models here.
class Event(models.Model):
    GENDER_CHOICES = [(0, 'Male'), (1, 'Female'), (3, 'All')]

    description = models.TextField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participated_events')
    image = models.ImageField(max_length=255, blank=True, null=True)
    date = models.DateField(_("Date"), default=datetime.date.today)
    start = models.TimeField(blank=True, null=True)
    finish = models.TimeField(blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=3)
    max_participants = models.IntegerField(default=0)
    num_participants = models.IntegerField(default=1)

    def __str__(self):
        return self.name