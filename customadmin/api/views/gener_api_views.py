from rest_framework import viewsets, permissions
from customadmin.api.serializers.gener_viewset_serializer import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by_id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(modified_by_id=self.request.user.id)
