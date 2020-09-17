from .models import Ingredient
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['title', 'category','calories', 'quantity']
