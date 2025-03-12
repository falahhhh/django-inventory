from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        related_name="users_user",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="users_user_user_permissions",
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
    