from django.urls import path
from .views import (
    TransactionListCreateView, TransactionDetailView,
    TransactionDetailListCreateView, TransactionDetailDetailView
)

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction-details/', TransactionDetailListCreateView.as_view(), name='transaction-detail-list'),
    path('transaction-details/<int:id>/', TransactionDetailDetailView.as_view(), name='transaction-detail-detail'),
]
