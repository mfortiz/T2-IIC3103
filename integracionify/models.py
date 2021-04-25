from django.db import models

# Create your models here.

class Artist(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    albums = models.CharField(max_length=100)
    tracks = models.CharField(max_length=100)
    self_url = models.CharField(max_length=100)

class Album(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    tracks = models.CharField(max_length=100)
    self_url = models.CharField(max_length=100)
    

class Track(models.Model):
    id = models.CharField(max_length=22, primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    times_played = models.IntegerField()
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    self_url = models.CharField(max_length=100)

    