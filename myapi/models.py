from django.db import models

# Create your models here.
class API(models.Model):
    Username = models.CharField(max_length=40)
    Email = models.EmailField(max_length=40)
    groups = models.CharField(max_length=40)

    def __str__(self):
        return self.Username