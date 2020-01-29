from rest_framework import serializers
from bands.models import MusicalBand


class MusicalBandSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='created_by.username')
    modifier = serializers.ReadOnlyField(source='modified_by.username')
    class Meta:
        model = MusicalBand
        fields = ['name','established_date','location','description','cover_image','creator','modifier']
