from django.db import models

# Create your models here.



class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    featerd = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


