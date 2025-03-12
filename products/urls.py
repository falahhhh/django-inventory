from django.urls import path
from .views import (
    ProductListCreateView,ProductDetailView,
    ProductCategoryListCreateView, ProductCategoryDetailView
)

urlpatterns = [

    path('product/', ProductListCreateView.as_view(), name='product-list'),
    path('product/<str:name>/', ProductDetailView.as_view(), name='product-detail'),

    path('category/', ProductCategoryListCreateView.as_view(), name='category-list'),
    path('category/<str:name>/', ProductCategoryDetailView.as_view(), name='category-detail'),
]