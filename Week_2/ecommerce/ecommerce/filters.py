import django_filters
from .models import ProductItem

class ProductItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__category_name', lookup_expr='iexact')

    class Meta:
        model = ProductItem
        fields = ['category', 'product_name']  # query params: ?category=Electronics&product_name=laptop
