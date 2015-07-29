from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2) 
    added_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    #todo: add "present" to end date
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + " (" + self.company + ")"
