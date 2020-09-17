from django.db import models
from ..recipes.models import Recipe

class Ingredient (models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.TextField(max_length=1000)
    calories =models.TextField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return self.title