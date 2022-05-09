from django.urls import path
from rest_framework import routers
from .views import GetStartedAPIView

router = routers.DefaultRouter()
router.register('api/portfolio', GetStartedAPIView, 'portfolio')
urlpatterns = router.urls