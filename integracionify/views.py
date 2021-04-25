from django.shortcuts import render
from rest_framework import viewsets
from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

# Create your views here.

class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer