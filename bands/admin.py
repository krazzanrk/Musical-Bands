from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MusicalBand)
admin.site.register(Role)
admin.site.register(BandMember)
admin.site.register(Member_status)
admin.site.register(Genre)
# admin.site.register(Song)

class SongTabularInline(admin.TabularInline):
    model = Song

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongTabularInline]


# class MemberStatusTabularInline(admin.TabularInline):
#     model = Member_status
#
# class BandMemberAdmin(admin.ModelAdmin):
#     inlines = [MemberStatusTabularInline]
#
# admin.site.register(BandMember,BandMemberAdmin)



admin.site.register(Album,AlbumAdmin)