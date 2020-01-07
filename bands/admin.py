from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MusicalBand)
admin.site.register(Role)
admin.site.register(BandMember)
admin.site.register(MemberStatus)
admin.site.register(Genre)

class SongTabularInline(admin.TabularInline):
    model = Song

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongTabularInline]

admin.site.register(Album,AlbumAdmin)

