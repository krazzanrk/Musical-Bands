from django.db import models


# Create your models here.

class Music_Band(models.Model):
    band_name = models.CharField(max_length=50)
    established_date = models.DateField()
    location = models.CharField(max_length=25)
    description = models.TextField()
    Image = models.ImageField()

    def __str__(self):
        return self.band_name

    class Meta:

        verbose_name_plural = "Music Bands"


class Role(models.Model):
    role_title = models.CharField(max_length=50)

    def __str__(self):
        return self.role_title

    class Meta:

        verbose_name_plural = "Roles"


class Band_member(models.Model):
    member_name = models.CharField(max_length=50)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.member_name

    class Meta:

        verbose_name_plural = "Band Members"


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    music_band = models.ForeignKey(Music_Band, on_delete=models.DO_NOTHING)
    published_year = models.DateField()
    Image = models.ImageField()

    def __str__(self):
        return self.album_name



class Genre(models.Model):
    genre_title = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_title


class Song(models.Model):
    song_title = models.CharField(max_length=50)
    gener = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    artist = models.ManyToManyField(Band_member)

    def __str__(self):
        return self.song_title
