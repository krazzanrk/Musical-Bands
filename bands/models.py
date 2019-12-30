from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class MusicalBand(models.Model):
    band_name = models.CharField(max_length=50)
    musical_band_established_date = models.DateField()
    location = models.CharField(max_length=25)
    description = models.TextField()
    logo = models.ImageField()
    cover_image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='band_created_by')
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True ,related_name='band_modified_by',null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.band_name

    class Meta:
        verbose_name_plural = "Music Bands"


class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Roles"


class BandMember(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    profile_pic = models.ImageField()
    description = models.TextField()
    role = models.ManyToManyField(Role)
    date_joined = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Band Members"


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_released=models.DateTimeField()
    music_band = models.ForeignKey(MusicalBand, on_delete=models.DO_NOTHING, related_name='musical_band')
    album_published_year = models.DateField()
    image = models.ImageField()
    album_created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='album_created')
    album_created_date = models.DateTimeField(auto_now=True)
    added_album_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True,null=True)
    added_album_modified_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.album_name


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    song_title = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING, related_name='band_album')
    artist = models.ManyToManyField(BandMember)
    song_added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='song_added')
    song_added_date = models.DateTimeField(auto_now=True)
    added_song_modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True,null=True)
    added_song_modified_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.song_title
