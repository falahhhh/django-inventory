from rest_framework import generics, permissions
from .models import Barang, KategoriBarang, Transaksi, DetailTransaksi, User
from .serializers import BarangSerializer, KategoriBarangSerializer, RegisterSerializer, TransaksiSerializer, DetailTransaksiSerializer

from .permissions import IsAdminOrReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminOrReadOnly]

class BarangListCreateView(generics.ListCreateAPIView):
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer
    permission_classes = [IsAdminOrReadOnly]

class BarangDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer
    lookup_field = "nama"
    permission_classes = [IsAdminOrReadOnly]

class KategoriBarangListCreateView(generics.ListCreateAPIView):
    queryset = KategoriBarang.objects.prefetch_related('barang').all()
    serializer_class = KategoriBarangSerializer
permission_classes = [IsAdminOrReadOnly]

class KategoriBarangDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KategoriBarang.objects.all()
    serializer_class = KategoriBarangSerializer
    lookup_field = "nama"
    permission_classes = [IsAdminOrReadOnly]

class TransaksiListCreateView(generics.ListCreateAPIView):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransaksiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    lookup_field = "id"
    permission_classes = [IsAdminOrReadOnly]


class DetailTransaksiListCreateView(generics.ListCreateAPIView):
    queryset = DetailTransaksi.objects.all()
    serializer_class = DetailTransaksiSerializer
    permission_classes = [IsAdminOrReadOnly]

class DetailTransaksiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailTransaksi.objects.all()
    serializer_class = DetailTransaksiSerializer
    lookup_field = "id"
    permission_classes = [IsAdminOrReadOnly]

