from rest_framework import permissions, status
from rest_framework.response import Response

from bands.models import MusicalBand
from customadmin.api.serializers.musical_band_serializer import MusicalBandSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class MusicalBandCreateApiView(ListAPIView, CreateAPIView):
    queryset = MusicalBand.objects.all()
    serializer_class = MusicalBandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = MusicalBandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by_id=self.request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicalBandListApiView(ListAPIView):
    queryset = MusicalBand.objects.all()
    serializer_class = MusicalBandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MusicalBandRetrieveView(RetrieveAPIView):
    queryset = MusicalBand.objects.all()
    serializer_class = MusicalBandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class MusicalBandUpdateApiView(RetrieveAPIView, UpdateAPIView):
    queryset = MusicalBand.objects.all()
    serializer_class = MusicalBandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MusicalBandSerializer(data=request.data, instance=instance, )
        if serializer.is_valid():
            serializer.save(modified_by_id=self.request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicalBandDestroyApiView(RetrieveAPIView, DestroyAPIView):
    queryset = MusicalBand.objects.all()
    serializer_class = MusicalBandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
