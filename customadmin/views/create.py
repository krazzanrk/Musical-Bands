from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *




class MusicalBandCreateView(CreateView):
    model = MusicalBand
    template_name = 'admin_edit/create/add_musicalband.html'
    fields = ['name', 'established_date', 'location', 'description', 'cover_image', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')


class BandMemberCreateView(CreateView):
    model = BandMember
    template_name = 'admin_edit/create/add_bandmember.html'
    fields = ['first_name', 'middle_name', 'last_name', 'dob', 'musical_band', 'status', 'joined_date', 'profile_pic',
              'description', 'role', 'created_by', 'created_date']

    success_url = reverse_lazy('bands:home')


class AlbumCreateView(CreateView):
    model = Album
    template_name = 'admin_edit/create/add_album.html'
    fields = ['name', 'released', 'musical_band', 'description', 'image', 'created_by', 'created_date']
    success_url = reverse_lazy('bands:home')


class SongAddView(CreateView):
    model = Song
    template_name = 'admin_edit/create/add_songs.html'
    fields = ['title','genre','album','member_name','created_by','created_date']
    success_url = reverse_lazy('bands:home')
