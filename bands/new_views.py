from django.shortcuts import render
from .models import *
from django.views.generic import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['popular_band'] = MusicalBand.objects.all()
        context['nepali_bands'] = MusicalBand.objects.order_by('established_date')[:3]
        context['latest_albums'] = Album.objects.order_by('-released')[:3]
        context['trending_songs'] = Song.objects.order_by('title')[:3]
        return context


class AlbumListView(ListView):
    template_name = 'album_list.html'
    model = Album
    paginate_by = 2
    context_object_name = 'albums'


class BandListView(ListView):
    template_name = 'band_list.html'
    model = MusicalBand
    paginate_by = 1
    context_object_name = 'musical_bands'


class BandDetailView(DetailView):
    template_name = 'band_detail.html'
    model = MusicalBand


class AllBandMemberView(DetailView):
    model = MusicalBand
    template_name = 'all_bandmember.html'


class AlbumDetailView(DetailView):
    template_name = 'album_detail.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.filter(song__album_id=self.object.id).distinct()
        context['members'] = BandMember.objects.filter(song__album_id=self.object.id).distinct()
        return context


class SearchResultView(ListView):
    model = MusicalBand

    def get(self, request, *args, **kwargs):
        title = request.GET.get('title')
        band = request.GET.get('band')

        if request.GET.get('band'):
            search_result = MusicalBand.objects.filter(name__icontains=band)
            return render(request, 'search_result_by_musical_band.html', context={
                'search_result': search_result
            })

        elif request.GET.get('title'):
            search_result = Album.objects.filter(musical_band__album__name__icontains=title)
            return render(request, 'search_result_by_album.html', context={
                'search_result': search_result
            })
