from django.db import models
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
    movie = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    genres = models.CharField(max_length=200)
    synopsis = models.TextField()
    release_date = models.DateField

    def publish(self):
        self.save()

    def __str__(self):
        return self.movie