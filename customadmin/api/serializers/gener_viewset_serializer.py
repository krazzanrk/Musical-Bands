from rest_framework import serializers
from django.contrib.auth.models import User
from bands.models import *


class GenreSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='created_by.username')
    modifier = serializers.ReadOnlyField(source='modified_by.username')


    class Meta:
        model = Genre
        fields = ['title', 'creator', 'created_date', 'modifier', 'modified_date']
        read_only_fields=['created_by']




