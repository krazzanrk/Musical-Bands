# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *


class MusicalBandUpdateView(LoginRequiredMixin,UpdateView):
    model = MusicalBand
    fields = ['name', 'established_date', 'location', 'description', 'cover_image', 'modified_by', 'modified_date']
    template_name = 'admin_edit/update/musicalband_update_form.html'
    success_url = reverse_lazy('customadmin:musical_band_added_list')


class BandMemberUpdateView(LoginRequiredMixin,UpdateView):
    model = BandMember
    template_name = 'admin_edit/update/bandmember_update_form.html'
    fields = ['first_name', 'middle_name', 'last_name', 'dob', 'musical_band', 'status', 'joined_date', 'profile_pic',
              'description', 'role', 'modified_by', 'modified_date']

    success_url = reverse_lazy('customadmin:added_bandmember_list')


class AlbumUpdateView(LoginRequiredMixin,UpdateView):
    model = Album
    template_name = 'admin_edit/update/album_update_form.html'
    fields = ['name', 'released', 'musical_band', 'description', 'image', 'modified_by', 'modified_date']
    success_url = reverse_lazy('customadmin:album_added_list')


class SongUpdateView(LoginRequiredMixin,UpdateView):
    model = Song
    template_name = 'admin_edit/update/song_update_form.html'
    fields = ['title', 'genre', 'album', 'member_name', 'modified_by', 'modified_date']
    success_url = reverse_lazy('customadmin:added_song_list')