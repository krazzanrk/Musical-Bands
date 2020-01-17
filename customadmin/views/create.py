from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *


class MusicalBandCreateView(LoginRequiredMixin, CreateView):
    model = MusicalBand
    template_name = 'admin_edit/create/add_musicalband.html'
    fields = ['name', 'established_date', 'location', 'description', 'cover_image', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')


class BandMemberCreateView(LoginRequiredMixin,CreateView):
    model = BandMember
    template_name = 'admin_edit/create/add_bandmember.html'
    fields = ['first_name', 'middle_name', 'last_name', 'dob', 'musical_band', 'status', 'joined_date', 'profile_pic',
              'description', 'role', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['musical_band'].queryset = MusicalBand.objects.filter(created_by=self.request.user)
        return form


class AlbumCreateView(LoginRequiredMixin,CreateView):
    model = Album
    template_name = 'admin_edit/create/add_album.html'
    fields = ['name', 'released', 'musical_band', 'description', 'image', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['musical_band'].queryset = MusicalBand.objects.filter(created_by=self.request.user)
        return form


class SongAddView(LoginRequiredMixin,CreateView):
    model = Song
    template_name = 'admin_edit/create/add_songs.html'
    fields = ['title', 'genre', 'album', 'member_name', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['member_name'].queryset = BandMember.objects.filter(created_by=self.request.user)
        form.fields['album'].queryset = Album.objects.filter(created_by=self.request.user)
        return form
