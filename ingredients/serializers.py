from .models import Ingredient
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from recipes.models import Recipe

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:

        model = Ingredient
        fields = ['title', 'category','calories', 'quantity', 'recipe']
