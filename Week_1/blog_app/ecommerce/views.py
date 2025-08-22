# blog_api/ecommerce/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductCategory, ProductItem
from .serializers import ProductCategorySerializer, ProductItemSerializer
from .filters import ProductItemFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #Categories rarely need search/order, but you may add if you want:
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category_name']
    ordering_fields = ['category_name', 'id']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.select_related('category').all()
    serializer_class = ProductItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductItemFilter
    search_fields = ['product_name', 'category__category_name']
    ordering_fields = ['price', 'product_name', 'id']
