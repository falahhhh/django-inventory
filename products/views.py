from rest_framework import generics
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from users.permissions import IsAdminOrReadOnly
# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]

class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.prefetch_related('product').all()
    serializer_class = ProductCategorySerializer
permission_classes = [IsAdminOrReadOnly]

class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    lookup_field = "name"
    permission_classes = [IsAdminOrReadOnly]
