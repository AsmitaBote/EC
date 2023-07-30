from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
