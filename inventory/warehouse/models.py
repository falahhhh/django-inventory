from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        related_name="warehouse_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="warehouse_user_permissions",
        blank=True
    )

    def save(self, *args, **kwargs):
        """Set is_staff dan is_superuser berdasarkan role"""
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class KategoriBarang(models.Model):
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kode = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=100)
    kategori = models.ForeignKey(KategoriBarang, on_delete=models.CASCADE, related_name="barang")
    stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.kode} - {self.nama}"

class Transaksi(models.Model):
    TIPE_TRANSAKSI = [
        ('masuk', 'Barang Masuk'),
        ('keluar', 'Barang Keluar'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaksi")
    tipe = models.CharField(max_length=10, choices=TIPE_TRANSAKSI)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipe.upper()} - {self.tanggal.strftime('%Y-%m-%d %H:%M')}"

class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE, related_name="detail")
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE, related_name="transaksi_detail")
    jumlah = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.transaksi.tipe == 'keluar':
            if self.barang.stok < self.jumlah:
                raise ValueError("Stok tidak mencukupi untuk transaksi keluar")
            self.barang.stok -= self.jumlah
        else:
            self.barang.stok += self.jumlah
        
        self.barang.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaksi} - {self.barang.nama} ({self.jumlah})"
