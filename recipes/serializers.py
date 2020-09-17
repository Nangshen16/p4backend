from .models import Recipe
#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ingredients.serializers import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cuisine','user', 'id']


