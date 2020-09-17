from django.db import models
from django.contrib.auth.models import User

class Ingredient (models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    cuisine =models.TextField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return self.category