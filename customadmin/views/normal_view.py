from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *


class AdminIndexView(LoginRequiredMixin,TemplateView):
    template_name = 'admin_index.html'


class AdminMusicalBandListView(LoginRequiredMixin,ListView):
    template_name = 'lists/added_band_list.html'
    context_object_name = 'musical_band'

    def get_queryset(self):
        return MusicalBand.objects.filter(created_by=self.request.user)


class AdminAlbumListView(LoginRequiredMixin,ListView):
    template_name = 'lists/added_album_list.html'
    context_object_name = 'added_album'

    def get_queryset(self):
        return Album.objects.filter(created_by=self.request.user)


class AdminSongListView(LoginRequiredMixin,ListView):
    template_name = 'lists/added_song_list.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.filter(created_by=self.request.user)


class AdminBandmemberListView(LoginRequiredMixin,ListView):
    template_name = 'lists/added_bandmember_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        return BandMember.objects.filter(created_by=self.request.user)
