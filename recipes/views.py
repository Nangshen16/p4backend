from .models import Recipe
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer, UserSerializer, GroupSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer





