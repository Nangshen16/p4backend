from .models import Recipe
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny



class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer





