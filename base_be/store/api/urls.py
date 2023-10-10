from django.urls import path, include
from rest_framework import routers
from .v1.product import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
