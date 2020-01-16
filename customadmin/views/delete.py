# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'admin_edit/delete/delete_confirmation.html'
    success_url = reverse_lazy('customadmin:album_added_list')


class MusicalBandDeleteView(DeleteView):
    model = MusicalBand
    template_name = 'admin_edit/delete/delete_confirmation.html'
    success_url = reverse_lazy('customadmin:musical_band_added_list')


class BandMemberDeleteView(DeleteView):
    model = BandMember
    template_name = 'admin_edit/delete/delete_confirmation.html'
    success_url = reverse_lazy('customadmin:added_bandmember_list')


class SongDeleteView(DeleteView):
    model = Song
    template_name = 'admin_edit/delete/delete_confirmation.html'
    success_url = reverse_lazy('customadmin:added_song_list')
