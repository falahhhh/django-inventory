from rest_framework import generics
from .models import Transaction, TransactionDetail
from users.permissions import IsAdminOrReadOnly
from .serializers import (
    TransactionSerializer, TransactionDetailSerializer
)

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"
    permission_classes = [IsAdminOrReadOnly]

class TransactionDetailListCreateView(generics.ListCreateAPIView):
    queryset = TransactionDetail.objects.all()
    serializer_class = TransactionDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

class TransactionDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionDetail.objects.all()
    serializer_class = TransactionDetailSerializer
    lookup_field = "id"
    permission_classes = [IsAdminOrReadOnly]
