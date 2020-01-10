from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import *
from bands.models import *
import datetime


class TestView(TemplateView):
    template_name = '_admin_base.html'


class MusicalBandCreateView(CreateView):
    template_name = 'add_musicalband.html'
    model = BandMember
    fields = ['first_name', 'middle_name', 'last_name', 'dob', 'musical_band', 'status', 'joined_date', 'profile_pic',
              'description', 'role']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print('888888888888888888888888888')

        if form.is_valid():
            print('tttttttttttttttttttttttttttttttttttttttttttttttttttt')
            sucess = form.save(commit=False)
            sucess.created_by_id = request.user.id
            sucess.created_date = datetime.date.today()
            print('hhhhhhhhhhhhhhhhhhhhhhhhhh')
            sucess.save()
        else:
            print(form.errors)
        return redirect('bands:home')
