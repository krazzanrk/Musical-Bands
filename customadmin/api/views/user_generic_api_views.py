from rest_framework import permissions

from customadmin.api.serializers.user_serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserRetriveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
