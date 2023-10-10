from django.db import models

# Create your models here.
class Index(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name