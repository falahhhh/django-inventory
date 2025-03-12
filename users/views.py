from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from .permissions import IsAdminOrReadOnly


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
