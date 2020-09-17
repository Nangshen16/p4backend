from .models import Recipe
#from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #   many=False,
    #   read_only=True,
    #   view_name='user-detail'
    #  )
    #user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cuisine','user']


