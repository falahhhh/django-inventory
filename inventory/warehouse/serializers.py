from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Barang, Transaksi, DetailTransaksi, KategoriBarang

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'


class KategoriBarangSerializer(serializers.ModelSerializer):
    barang = BarangSerializer(many=True, read_only=True)
    class Meta:
        model = KategoriBarang
        fields = ['id', 'nama', 'barang']
        
class TransaksiSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaksi
        fields = '__all__'

class DetailTransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailTransaksi
        fields = '__all__'

    def validate(self, data):
        """Pastikan stok cukup untuk transaksi keluar"""
        if data['transaksi'].tipe == 'keluar' and data['barang'].stok < data['jumlah']:
            raise serializers.ValidationError("Stok barang tidak mencukupi.")
        return data
