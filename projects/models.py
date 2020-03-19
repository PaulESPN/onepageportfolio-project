from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
