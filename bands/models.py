from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MusicalBand(models.Model):
    name = models.CharField(max_length=50)
    established_date = models.DateField()
    location = models.CharField(max_length=25)
    description = models.TextField()
    logo = models.ImageField()
    cover_image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Musical Bands"


class Member_status(models.Model):
    band_date_joined = models.DateField()
    band = models.ForeignKey(MusicalBand, on_delete=models.DO_NOTHING)
    status = models.BooleanField()

    def __str__(self):
        return self.band.name


class BandMember(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Member_status, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField()
    description = models.TextField()
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Band members"


class Album(models.Model):
    name = models.CharField(max_length=50)
    released = models.DateTimeField()
    musical_band = models.ForeignKey(MusicalBand, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey(User, blank=True,on_delete=models.DO_NOTHING)
    modified_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Album names'


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    member_name = models.ManyToManyField(BandMember)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    added_date = models.DateField(auto_now=True)
    # modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    modified_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
