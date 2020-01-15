from django.urls import path
from .views import *

app_name = 'customadmin'

urlpatterns = [

    path('index', AdminIndexView.as_view(), name='custom_admin_index'),
    path('add/bandmember', BandMemberCreateView.as_view(), name='band_member_create'),
    path('add/musical_band', MusicalBandCreateView.as_view(), name='musical_band_create'),
    path('add/album', AlbumCreateView.as_view(), name='album_create'),
    path('add/song', SongAddView.as_view(), name='add_song'),

    path('update/musical_band/<slug:slug>', MusicalBandUpdateView.as_view(), name='musical_band_update'),
    path('update/bandmember/<int:pk>', BandMemberUpdateView.as_view(), name='bandmember_update'),
    path('update/album/<slug:slug>',AlbumUpdateView.as_view(),name='album_update_view'),

    path('musical_band/list', AdminMusicalBandListView.as_view(), name='musical_band_added_list'),
    path('album/list', AdminAlbumListView.as_view(), name='album_added_list'),
    path('songs/list',AdminSongListView.as_view(),name='added_song_list'),
    path('bandmember/list',AdminBandmemberListView.as_view(),name='added_bandmember_list')

]
