from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.utils.timezone import make_aware
from datetime import datetime

# Create your models here.
# models.py
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(blank=True)
    user = models.CharField(max_length=1000000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # If date is not provided, assign a timezone-aware datetime
        if not self.date:
            self.date = make_aware(datetime.now())
        super().save(*args, **kwargs)

