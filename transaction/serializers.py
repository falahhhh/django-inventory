from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Transaction, TransactionDetail, Product

User = get_user_model()

class TransactionDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = TransactionDetail
        fields = ['id', 'product', 'product_name', 'quantity']

class TransactionSerializer(serializers.ModelSerializer):
    details = TransactionDetailSerializer(many=True, read_only=True)
    details_input = serializers.ListField(write_only=True, child=serializers.DictField())

    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'date', 'details', 'details_input']

    def create(self, validated_data):
        details_data = validated_data.pop('details_input', [])

        # Pastikan transaksi hanya dibuat sekali
        transaction = Transaction.objects.create(**validated_data)

        product_updates = []  # Simpan produk yang akan diperbarui

        for detail in details_data:
            product_id = detail.get('product')
            quantity = detail.get('quantity')

            # Validasi jika produk tidak ditemukan
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError({"details": f"Product with ID {product_id} does not exist."})

            # Hitung stok baru tanpa langsung menyimpan
            if validated_data['transaction_type'] == "out":
                if product.stock < quantity:
                    raise serializers.ValidationError({"details": f"Insufficient stock for product {product.name}!"})
                product.stock -= quantity  # Kurangi stok
            else:
                product.stock += quantity  # Tambah stok

            # Tambahkan ke list untuk batch update
            product_updates.append(product)

            # Simpan detail transaksi
            TransactionDetail.objects.create(transaction=transaction, product=product, quantity=quantity)

        # Lakukan update stok hanya sekali di akhir loop
        for product in product_updates:
            product.save()

        return transaction
