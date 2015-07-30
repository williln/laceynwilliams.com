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
    end_date = models.DateTimeField(default=timezone.now, blank=True)
    still_working = models.BooleanField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title + " (" + self.company + ")"

class Talk(models.Model):
    title = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    description = models.TextField()
    added_date = models.DateTimeField(default=timezone.now)
    talk_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)
    slides = models.URLField(max_length=200)
    video = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=200)
    publications = models.CharField(max_length=200)
    description = models.TextField()
    added_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title   

class Education(models.Model):
    university =  models.CharField(max_length=200) 
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2) 
    grad_date = models.DateTimeField(default=timezone.now)
    degree = models.CharField(max_length=200) 
    notes = models.TextField()

    def __str__(self):
        return self.degree + ', ' + self.university
