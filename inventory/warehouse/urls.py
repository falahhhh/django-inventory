from django.urls import path
from .views import (
    
    BarangListCreateView, BarangDetailView,
    KategoriBarangListCreateView, KategoriBarangDetailView, RegisterView,
    TransaksiListCreateView, TransaksiDetailView,
    DetailTransaksiListCreateView, DetailTransaksiDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/save', RegisterView.as_view(), name='register-save'),


    path('barang/', BarangListCreateView.as_view(), name='barang-list'),
    path('barang/<str:nama>/', BarangDetailView.as_view(), name='barang-detail'),

    path('kategori/', KategoriBarangListCreateView.as_view(), name='kategori-list'),
    path('kategori/<str:nama>/', KategoriBarangDetailView.as_view(), name='kategori-detail'),

    path('transaksi/', TransaksiListCreateView.as_view(), name='transaksi-list'),
    path('transaksi/<int:id>/', TransaksiDetailView.as_view(), name='transaksi-detail'),
    path('detail-transaksi/', DetailTransaksiListCreateView.as_view(), name='detail-transaksi-list'),
    path('detail-transaksi/<int:id>/', DetailTransaksiDetailView.as_view(), name='detail-transaksi-detail'),
]
