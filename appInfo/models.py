from django.db import models

# Create your models here.
class Device(models.Model):
    version = models.FloatField()
    platform = models.CharField(max_length = 50)

    def __str__(self):
        return self.platform