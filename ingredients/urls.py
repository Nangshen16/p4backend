from django.conf.urls import url
from rest_framework import routers
from .views import IngredientViewSet

router = routers.DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
urlpatterns = router.urls