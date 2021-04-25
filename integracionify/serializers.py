from rest_framework import serializers
from .models import Artist, Album, Track

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' 

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = '__all__' 