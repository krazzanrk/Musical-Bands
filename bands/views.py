# from django.shortcuts import render
# from .models import *
#
# # Create your views here.
# from django.views.generic import *
#
#
# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['popular_band'] = MusicalBand.objects.all()
#         context['nepali_bands'] = MusicalBand.objects.order_by('established_date')[:3]
#         context['latest_albums'] = Album.objects.order_by('-released')[:3]
#         context['trending_songs'] = Song.objects.order_by('-added_date')[:3]
#         # context['musical_band'] = MusicalBand.objects.all()
#
#         return context
#
# class AlbumListView(ListView):
#     template_name = 'album_list.html'
#     model = Album
#     paginate_by = 2
#     context_object_name = 'albums'
#
#
# class BandListView(ListView):
#     template_name = 'band_list.html'
#     model = MusicalBand
#     context_object_name = 'musical_bands'
#     paginate_by = 2
#
#
# class AlbumDetailView(TemplateView):
#     template_name = 'album_detail.html'
#     model = Album
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs['slug']
#
#         album = Album.objects.get(slug=slug)
#         context['album_detail'] = album
#         context['albums'] = Album.objects.filter(musical_band=album.musical_band.id)[:3]
#         songs = Song.objects.filter(album=album.id)
#         context['songs'] = songs
#         member_name = []
#         alb = BandMember.objects.filter(song__album_id=album.id)
#         for i in alb:
#             member_name.append(i)
#         context['members'] = set(member_name)
#         genre = []
#         alb = Genre.objects.filter(song__album_id=album.id)
#         for i in alb:
#             genre.append(i)
#         context['genres'] = set(genre)
#         return context

# another way
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     # context['albums'] = Album.objects.all()
#     # context['albums'] = Album.objects.filter(musical_band_id=self.object.musical_band_id)[:3]
#     # context['songs'] = Song.objects.filter(album_id=self.object.id)[:3]
#     context['genres'] = Genre.objects.filter(song__album_id=self.object.id).distinct()
#     context['members'] = BandMember.objects.filter(song__album_id=self.object.id).distinct()
#     return context
#
#
# class BandDetailView(DetailView):
#     template_name = 'band_detail.html'
#     model = MusicalBand
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs['slug']
#         music_band = MusicalBand.objects.get(slug=slug)
#         context['music_band_detail'] = music_band
#         bandmember = BandMember.objects.filter(status__band_id=music_band)
#         context['bandmembers'] = bandmember
#         context['latest_released']=Album.objects.filter(musical_band=music_band).order_by('-released')[:5]
#
#
#         return context


#another way to write context


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
# context['bandmembers'] = BandMember.objects.filter(musical_band_id=self.object.id)
# context['latest_released'] = Album.objects.filter(musical_band=self.object.id).order_by('-released')[:5]
# return context

#
#
#
#
#
# class SearchResultView(ListView):
#     template_name = 'search_result_by_musical_band.html'
#     model = MusicalBand
#
#     def get(self, request, *args, **kwargs):
#         title = request.GET.get('title')
#         band = request.GET.get('band')
#
#         if request.GET.get('band'):
#             search_result = MusicalBand.objects.filter(name__icontains=band)
#             return render(request, 'search_result_by_musical_band.html', context={
#                 'search_result': search_result
#             })
#
#         elif request.GET.get('title'):
#             search_result = Album.objects.filter(musical_band__album__name__icontains=title)
#             return render(request, 'search_result_by_album.html', context={
#                 'search_result': search_result
#             })
