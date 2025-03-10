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

class DetailTransaksiSerializer(serializers.ModelSerializer):
    nama_barang = serializers.CharField(source='barang.nama', read_only=True)

    class Meta:
        model = DetailTransaksi
        fields = ['id', 'barang', 'nama_barang', 'jumlah']

class TransaksiSerializer(serializers.ModelSerializer):
    detail = DetailTransaksiSerializer(many=True, read_only=True)
    detail_input = DetailTransaksiSerializer(many=True, write_only=True)

    class Meta:
        model = Transaksi
        fields = ['id',  'tipe', 'tanggal', 'detail', 'detail_input']

    def create(self, validated_data):
        detail_data = validated_data.pop('detail_input')
        transaksi = Transaksi.objects.create(**validated_data)

        for detail in detail_data:
            barang = detail['barang']
            jumlah = detail['jumlah']

            if transaksi.tipe == "keluar":
                if barang.stok < jumlah:
                    raise serializers.ValidationError({"detail": f"Stok barang {barang.nama} tidak cukup!"})
                barang.stok -= jumlah
            else:
                barang.stok += jumlah

            barang.save()
            DetailTransaksi.objects.create(transaksi=transaksi, **detail)

        return transaksi
