from django.urls import reverse_lazy
from django.views.generic import *
from bands.models import *



class AdminIndexView(TemplateView):
    template_name = 'admin_index.html'

class AdminMusicalBandListView(ListView):
    template_name = 'lists/added_band_list.html'
    context_object_name = 'musical_band'

    def get_queryset(self):
        return MusicalBand.objects.filter(created_by=self.request.user)


class AdminAlbumListView(ListView):
    template_name = 'lists/added_album_list.html'
    context_object_name = 'added_album'

    def get_queryset(self):
        return Album.objects.filter(created_by=self.request.user)

