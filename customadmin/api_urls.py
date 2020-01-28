from django.urls import path
from customadmin.api.views.gener_api_views import *
from .api.views.role_func_view import *

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

urlpatterns = viewsets_genre_url + function_role_urls
