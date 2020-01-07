from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.utils.text import slugify


class Role(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='role_createdBy' )
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='role_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class MusicalBand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    established_date = models.DateField()
    location = models.CharField(max_length=25)
    description = models.TextField()
    cover_image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='musicalband_createdBy' )
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='musicalband_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Musical Bands"

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class MemberStatus(models.Model):
    band_date_joined = models.DateField()
    band = models.ForeignKey(MusicalBand, on_delete=models.DO_NOTHING)
    status = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='memberstatus_createdBy' )
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='memberstatus_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.band.name


class BandMember(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    status = models.ForeignKey(MemberStatus, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField()
    description = models.TextField()
    role = models.ManyToManyField(Role)

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='bandmember_createdBy')
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='bandmember_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Band members"


class Album(models.Model):
    name = models.CharField(max_length=50,unique=True)
    released = models.DateTimeField()
    musical_band = models.ForeignKey(MusicalBand, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='album_createdBy')
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='album_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Album names'

    # def get_absolute_url(self):
    #     return reverse('bands:bands_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Genre(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='genre_createdBy')
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='genre_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    member_name = models.ManyToManyField(BandMember)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='song_createdBy')
    created_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='song_modifiedBy',blank=True,null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
