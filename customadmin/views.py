from django.shortcuts import render, redirect

# Create your views here.
# from django.urls import reverse_lazy
# from django.views.generic import *
# from bands.models import *
# import datetime
#
#
# class TestView(TemplateView):
#     template_name = 'admin_index.html'
#
#
#
#
#
# class MusicalBandUpdateView(UpdateView):
#     model = MusicalBand
#     fields = ['name', 'established_date', 'location', 'description', 'cover_image', 'modified_by', 'modified_date']
#     template_name = 'admin_edit/update/musicalband_update_form.html'
#     success_url = reverse_lazy('bands:home')
#
#
# class BandMemberUpdateView(UpdateView):
#     model = BandMember
#     template_name = 'admin_edit/update/bandmember_update_form.html'
#     fields = ['first_name', 'middle_name', 'last_name', 'dob', 'musical_band', 'status', 'joined_date', 'profile_pic',
#               'description', 'role', 'modified_by', 'modified_date']
#
#     success_url = reverse_lazy('bands:home')