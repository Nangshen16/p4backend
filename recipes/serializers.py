from .models import Recipe
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cuisine']


