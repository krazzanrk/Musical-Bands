from django.urls import path
from customadmin.api.views.gener_api_views import *
from .api.views.role_func_view import *
from .api.views.musical_band_generic_api_views import *
from .api.views.user_generic_api_views import *

genre_list = GenreViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'

    }
)

genre_detail = GenreViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

viewsets_genre_url = [

    path('api/genre/', genre_list, name='genre_list_api'),
    path('api/genre/<int:pk>/', genre_detail, name='genre_detail_api'),

]

function_role_urls = [
    path('api/role/', role_list, name='api-role-list'),
    path('api/role/<int:pk>/', role_detail, name='api-role-detail')
]

generic_api_urls = [

    path('api/musicalband/post', MusicalBandCreateApiView.as_view(), name='api-muscialband-create'),
    path('api/musicalband/list', MusicalBandListApiView.as_view(), name='api-musicalband-list'),
    path('api/musicalband/<slug:slug>/retrive', MusicalBandRetrieveView.as_view(), name='api-musicalband-retrive'),
    path('api/musicalband/<slug:slug>/delete', MusicalBandDestroyApiView.as_view(), name='api-musicalband-destroy'),
    path('api/musicalband/<slug:slug>/update', MusicalBandUpdateApiView.as_view(), name='api-musicalband-update'),

]

user_api_url = [

    path('api/musicalband/user', UserListApiView.as_view(), name='user-api'),


]

urlpatterns = viewsets_genre_url + function_role_urls + generic_api_urls + user_api_url
