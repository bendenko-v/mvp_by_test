from rest_framework_mongoengine import generics

from core.models.user import User
from core.serializers import UserCreateSerializer, UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = 'id'


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
