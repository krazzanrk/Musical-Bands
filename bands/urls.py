from django.urls import path
# from .views import *
from .new_views import *

app_name = 'bands'

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('albumlist/', AlbumListView.as_view(), name='album_list'),
    path('bandlist/', BandListView.as_view(), name='band_list'),
    path('album/<slug:slug>', AlbumDetailView.as_view(), name='albums_detail'),
    path('band/<slug:slug>', BandDetailView.as_view(), name='bands_detail'),
    path('search/result', SearchResultView.as_view(), name='search'),
    path('bandmember/active',AllBandMemberView.as_view(),name='active_status')



]
