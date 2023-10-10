from rest_framework import generics
from .serializer import ProductSerializer
from rest_framework import viewsets
from ....models.product import Product


class ProductViewSet(viewsets.GenericViewSet, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
