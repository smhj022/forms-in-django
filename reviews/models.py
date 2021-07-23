from django.db import models

# Create your models here.


class Reviews(models.Model):
    username = models.CharField(max_length=100)
    reviews = models.TextField()
    rating = models.IntegerField()
