from django.shortcuts import render
from rest_framework import generics


from .models.store import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
