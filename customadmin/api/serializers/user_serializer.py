from rest_framework import serializers
from django.contrib.auth.models import User
from customadmin.api.serializers.gener_serializer import GenreSerializer
from customadmin.api.serializers.role_serailizer import RoleSerializer
from customadmin.api.serializers.musical_band_serializer import MusicalBandSerializer


class UserSerializer(serializers.ModelSerializer):
    genre_createdby = GenreSerializer(many=True, read_only=True)
    role_createdby = RoleSerializer(many=True, read_only=True)
    musicalband_createdby = MusicalBandSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','genre_createdby','role_createdby','musicalband_createdby']
